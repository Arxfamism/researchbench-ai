import streamlit as st
from database.database import initialize_database

# Initialize database
initialize_database()

# Page configuration
st.set_page_config(
    page_title="ResearchBench AI",
    page_icon="🧠",
    layout="wide"
)

# Home page
st.title("🧠 ResearchBench AI")

st.subheader("AI-powered research workspace")

st.write(
    "A research workspace designed for biotechnology "
    "and life-science students."
)

st.divider()

st.markdown("### 🚀 Welcome")

st.write(
    "Use the sidebar to access your research library, "
    "AI research assistant, research memory, protocol "
    "companion, research journey and dashboard."
)

st.info(
    "📚 Start by uploading a research paper or "
    "laboratory protocol from the Research Library."
)

st.divider()

st.markdown("### 🔬 Available Modules")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 📚 Research Library")
    st.write("Upload and manage research documents.")

with col2:
    st.markdown("#### 🤖 Research AI")
    st.write("Ask questions about your research.")

with col3:
    st.markdown("#### 🧠 Research Memory")
    st.write("Save ideas, notes and observations.")
