import streamlit as st
from summarizer import summarize_text  # Import the function from summarizer.py
from utils.helpers import read_file

st.set_page_config(page_title="Text Summarization App", layout="wide")
st.title("📝 Text Summarization App")

# Input section
st.markdown("### Enter your text below or upload a file")

# Centered layout for input text box
input_text = st.text_area("Enter your text here", height=100)

st.markdown("#### OR")
uploaded_file = st.file_uploader("Upload a file (.txt, .pdf, .docx)", type=["txt", "pdf", "docx"])

# Process on submission
if st.button("Summarize"):
    if uploaded_file:
        # Function to read file (we need to implement or uncomment this function)
        text = read_file(uploaded_file)
    elif input_text.strip():
        text = input_text
    else:
        st.warning("Please provide text or upload a file to summarize.")
        st.stop()

    # Allow the user to choose the summarization method
    summary_method = st.radio(
        "Select Summarization Method", 
        ("both", "abstractive", "extractive"),
        index=0
    )

    # Generate summaries
    with st.spinner("Generating summaries..."):
        summaries = summarize_text(text, method=summary_method)

    # Display summaries in two columns if both are selected
    col1, col2 = st.columns(2)

    if "extractive" in summaries:
        with col1:
            st.subheader("📑 Extractive Summary")
            st.write(summaries["extractive"])

    if "abstractive" in summaries:
        with col2:
            st.subheader("🧠 Abstractive Summary")
            st.write(summaries["abstractive"])

