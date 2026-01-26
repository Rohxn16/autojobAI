import streamlit as st
import requests

# Configuration
BASE_URL = "http://127.0.0.1:8000"
st.set_page_config(page_title="AutoJobAI", page_icon="🚀", layout="wide")

# Title and Description
st.title("🚀 AutoJobAI")
st.markdown("### Your Intelligent Job Search Assistant")
st.markdown("Upload your resume, and let AI find the perfect job matches for you based on your experience and skills.")

# Session State for Resume Upload
if "resume_uploaded" not in st.session_state:
    st.session_state.resume_uploaded = False

# --- Sidebar: Resume Upload ---
st.sidebar.header("📂 Upload Resume")
uploaded_file = st.sidebar.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    if st.sidebar.button("Process Resume"):
        with st.spinner("Processing resume..."):
            try:
                files = {"resume": (uploaded_file.name, uploaded_file, "application/pdf")}
                response = requests.post(f"{BASE_URL}/upload_resume", files=files)
                
                if response.status_code == 200:
                    st.sidebar.success("Resume processed successfully!")
                    st.session_state.resume_uploaded = True
                    data = response.json()
                    # Optional: Display extracted text summary
                    # st.sidebar.text_area("Extracted Text Review", data.get("extracted_text", "")[:500] + "...", height=150)
                else:
                    st.sidebar.error(f"Error: {response.json().get('detail', 'Unknown error')}")
            except requests.exceptions.RequestException as e:
                st.sidebar.error(f"Failed to connect to backend: {e}")

# --- Main Area: Job Search ---

if st.session_state.resume_uploaded:
    st.divider()
    st.header("🔍 Find Your Dream Job")
    
    if st.button("Search for Jobs"):
        with st.spinner("Analyzing profile and searching for jobs... (This may take a moment)"):
            try:
                response = requests.post(f"{BASE_URL}/query")
                
                if response.status_code == 200:
                    jobs = response.json()
                    
                    if not jobs:
                        st.info("No jobs found matching your profile. Try again later.")
                    else:
                        st.success(f"Found {len(jobs)} relevant positions!")
                        
                        # Display Jobs
                        for job in jobs:
                            with st.container():
                                col1, col2 = st.columns([4, 1])
                                with col1:
                                    st.subheader(job.get("title", "Unknown Role"))
                                    st.caption(f"📅 {job.get('date', 'N/A')} | 🏢 {job.get('company', 'Unknown Company')}")
                                with col2:
                                    st.write("") # Spacer
                                    if job.get("url"):
                                        st.link_button("Apply Now 🔗", job["url"])
                                    else:
                                        st.button("No Link", disabled=True)
                                st.divider()
                else:
                    st.error(f"Error fetching jobs: {response.json().get('detail', 'Unknown error')}")
                    
            except requests.exceptions.RequestException as e:
                st.error(f"Failed to connect to backend: {e}")
else:
    st.info("👈 Please upload your resume in the sidebar to get started.")

# Footer
st.markdown("---")
st.markdown("*Powered by Agentic AI*")
