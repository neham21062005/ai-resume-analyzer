import streamlit as st
from PyPDF2 import PdfReader
from utils import clean_text, calculate_similarity

st.title("📄 AI Resume Analyzer")

# Upload resume
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

# Job description input
job_description = st.text_area("Paste Job Description")

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

if uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)

    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(job_description)

    score = calculate_similarity(clean_resume, clean_jd)

    st.subheader(f"Match Score: {score}%")

    if score > 70:
        st.success("Good match! 👍")
    elif score > 40:
        st.warning("Moderate match ⚠️")
    else:
        st.error("Low match ❌")
