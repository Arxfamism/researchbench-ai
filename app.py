import streamlit as st

st.set_page_config(
    page_title="ResearchBench AI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 ResearchBench AI")
st.write("AI-powered research workspace for biotechnology students.")

st.sidebar.title("ResearchBench AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Research Library",
        "Research AI",
        "Research Memory",
        "Protocol Companion",
        "Research Journey",
        "Dashboard"
    ]
)

if page == "Research Library":
    st.header("📚 Research Library")
    st.info("Upload and manage your research papers and laboratory protocols.")

elif page == "Research AI":
    st.header("💬 Research AI")
    st.info("Ask questions about your uploaded research papers.")

elif page == "Research Memory":
    st.header("📝 Research Memory")
    st.info("Save your notes, questions, ideas, hypotheses and observations.")

elif page == "Protocol Companion":
    st.header("🧪 Protocol Companion")
    st.info("Convert laboratory protocols into interactive checklists.")

elif page == "Research Journey":
    st.header("🔗 Research Journey")
    st.info("Connect papers, thoughts, protocols and observations.")

elif page == "Dashboard":
    st.header("📊 Dashboard")
    st.info("Your research activity will appear here.")
