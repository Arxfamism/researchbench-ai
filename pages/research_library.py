import streamlit as st
import sqlite3
import uuid
from datetime import datetime
from services.pdf_processor import extract_text, get_page_count
from database.database import DB_PATH

st.title("📚 Research Library")

st.write(
    "Upload and manage your research papers and laboratory protocols."
)

uploaded_file = st.file_uploader(
    "Upload a PDF document",
    type=["pdf"]
)

document_type = st.selectbox(
    "Document Type",
    ["Research Paper", "Laboratory Protocol"]
)

if uploaded_file is not None:

    if st.button("📥 Process & Save Document"):

        try:
            text = extract_text(uploaded_file)
            page_count = get_page_count(uploaded_file)

            if not text.strip():
                st.error(
                    "Could not extract text from this PDF. "
                    "Please upload a text-readable PDF."
                )
            else:
                document_id = str(uuid.uuid4())
                upload_date = datetime.now().isoformat()

                conn = sqlite3.connect(DB_PATH)
                cursor = conn.cursor()

                cursor.execute(
                    """
                    INSERT INTO documents
                    (id, name, type, upload_date, text)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        document_id,
                        uploaded_file.name,
                        document_type,
                        upload_date,
                        text
                    )
                )

                conn.commit()
                conn.close()

                st.success("✅ Document saved successfully!")

                st.write("**File:**", uploaded_file.name)
                st.write("**Type:**", document_type)
                st.write("**Pages:**", page_count)

                with st.expander("📄 Extracted Text Preview"):
                    st.text(text[:5000])

        except Exception as e:
            st.error(f"Error: {e}")


st.divider()

st.subheader("📂 Saved Documents")

try:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, name, type, upload_date
        FROM documents
        ORDER BY upload_date DESC
        """
    )

    documents = cursor.fetchall()
    conn.close()

    if documents:
        for doc in documents:
            st.markdown(
                f"**📄 {doc[1]}**  \n"
                f"Type: {doc[2]}  \n"
                f"Uploaded: {doc[3]}"
            )
            st.divider()
    else:
        st.info("No documents uploaded yet.")

except Exception as e:
    st.error(f"Could not load documents: {e}")
