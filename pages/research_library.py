import streamlit as st
import pdfplumber

st.title("📚 Research Library")

st.write("Upload and manage your research papers and laboratory protocols.")

uploaded_file = st.file_uploader(
    "Upload a PDF document",
    type=["pdf"]
)

document_type = st.selectbox(
    "Document Type",
    ["Research Paper", "Laboratory Protocol"]
)

if uploaded_file is not None:
    st.info("Processing document...")

    try:
        text = ""

        with pdfplumber.open(uploaded_file) as pdf:
            page_count = len(pdf.pages)

            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        if not text.strip():
            st.error(
                "This document could not be processed. "
                "Please try another PDF or a text-readable version."
            )
        else:
            st.success("Document processed successfully!")

            st.write("**Filename:**", uploaded_file.name)
            st.write("**Document Type:**", document_type)
            st.write("**Pages:**", page_count)

            with st.expander("📄 Extracted Text Preview"):
                st.text(text[:5000])

            st.success("Document is ready to be added to the Research Library.")

    except Exception as e:
        st.error(f"Error processing PDF: {e}")
