import io
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text
import pdfplumber
import google.generativeai as genai
import base64

# Load environment variables
load_dotenv()

# Set up the Streamlit App
st.set_page_config(page_title="ATS Optimization & Cold Email Assistant")

# Initialize session state to manage first-time access
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

# Landing page content
if st.session_state.page == 'landing':
    st.title("Welcome to the ATS Optimization & Cold Email Assistant")
    st.markdown("""
        This app provides two key features:
        1. **ATS Analyzer** - Optimize your resume for job applications using Google Gemini.
        2. **Cold Email Generator** - Automate cold email generation using Groq's LLaMA 3.1.
        
        Please click below to get started.
    """)
    
    # Button to move to task selection
    if st.button("Get Started"):
        st.session_state.page = 'task_selection'

# Task selection page
if st.session_state.page == 'task_selection':
    # Sidebar for navigation
    st.sidebar.title("Choose the Task")
    task = st.sidebar.radio("Select the task you would like to perform:", ("ATS Analyzer", "Cold Email Generator"))

    # Function to configure Google Gemini for ATS Analyzer
    def configure_gemini():
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")
        genai.configure(api_key=api_key)

    def get_gemini_response(input_text, pdf_content, prompt):
        model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
        response = model.generate_content([input_text, pdf_content, prompt])
        return response.text

    # Function to parse resume
    def parse_resume(uploaded_file):
        if uploaded_file is not None:
            with pdfplumber.open(uploaded_file) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
            return text
        else:
            raise FileNotFoundError("No file uploaded")

    # ATS Analyzer section with Google Gemini
    if task == "ATS Analyzer":
        configure_gemini()

        st.markdown("""
            <style>
            .header {
                text-align: center;
                font-size: 46px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            </style>
            <div class="header">ATS System</div>
        """, unsafe_allow_html=True)

        input_text = st.text_area("Job Description: ", key="input")
        uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

        if uploaded_file:
            st.markdown(
                '<p style="color: green; font-size: 18px;">PDF Uploaded Successfully ✓</p>',
                unsafe_allow_html=True
            )

        submit1 = st.button("Tell Me About the Resume")
        submit2 = st.button("How Can I Improvise my Skills")
        submit3 = st.button("What are the Keywords That are Missing")
        submit4 = st.button("Percentage match")
        input_promp = st.text_input("Queries: Feel Free to Ask here")
        submit5 = st.button("Answer My Query")

        input_prompt1 = """
        You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description.
        Please share your professional evaluation on whether the candidate's profile aligns with the role.
        Highlight the strengths, weaknesses, and missing keywords of the applicant in relation to the specified job requirements.
        """

        input_prompt2 = """
        You are a Technical Human Resource Manager with expertise in data science.
        Share your insights on the candidate's suitability for the role from an HR perspective and offer advice on enhancing their skills.
        """

        input_prompt3 = """
        You are an ATS scanner with a deep understanding of data science and ATS functionality.
        Evaluate the resume against the provided job description. List the missing keywords and suggest skill improvement areas.
        """

        input_prompt4 = """
        Evaluate the resume against the job description. Give a percentage match, missing keywords, and your final evaluation.
        """

        if submit1:
            if uploaded_file is not None:
                pdf_content = parse_resume(uploaded_file)
                response = get_gemini_response(input_text, pdf_content, input_prompt1)
                st.subheader("The Response is")
                st.write(response)
            else:
                st.write("Please upload a PDF file to proceed.")

        elif submit2:
            if uploaded_file is not None:
                pdf_content = parse_resume(uploaded_file)
                response = get_gemini_response(input_text, pdf_content, input_prompt2)
                st.subheader("The Response is")
                st.write(response)
            else:
                st.write("Please upload a PDF file to proceed.")

        elif submit3:
            if uploaded_file is not None:
                pdf_content = parse_resume(uploaded_file)
                response = get_gemini_response(input_text, pdf_content, input_prompt3)
                st.subheader("The Response is")
                st.write(response)
            else:
                st.write("Please upload a PDF file to proceed.")

        elif submit4:
            if uploaded_file is not None:
                pdf_content = parse_resume(uploaded_file)
                response = get_gemini_response(input_text, pdf_content, input_prompt4)
                st.subheader("The Response is")
                st.write(response)
            else:
                st.write("Please upload a PDF file to proceed.")

        elif submit5:
            if uploaded_file is not None:
                pdf_content = parse_resume(uploaded_file)
                response = get_gemini_response(input_promp, pdf_content, input_text)
                st.subheader("The Response is")
                st.write(response)
            else:
                st.write("Please upload a PDF file to proceed.")

        footer = """
        ---
        #### Made By [Pavankumar](https://www.linkedin.com/in/pavankumar-kurapati/)
        For Queries, Reach out on [LinkedIn](https://www.linkedin.com/in/pavankumar-kurapati/)
        Resume Analyzer - Making Job Applications Easier
        """
        st.markdown(footer, unsafe_allow_html=True)


    # Cold Email Generator using Groq's LLaMA 3.1 model
    elif task == "Cold Email Generator":
        chain = Chain()
        portfolio = Portfolio()  # Create an instance of the Portfolio class

        def create_streamlit_app(llm, portfolio, clean_text):
            st.title("📧 Cold Email Generator")

            input_type = st.radio("Select Input Type:", ("Enter a URL", "Enter Job Description"))

            if input_type == "Enter a URL":
                url_input = st.text_input("Enter a URL:")
                submit_button = st.button("Submit URL")

                if submit_button:
                    try:
                        loader = WebBaseLoader([url_input])
                        data = clean_text(loader.load().pop().page_content)
                        portfolio.load_portfolio()  # Call the method on the instance
                        jobs = chain.extract_jobs(data)
                        generate_emails(jobs, portfolio, chain)  # Call the generate_emails function
                    except Exception as e:
                        st.error(f"An error occurred: {e}")

            elif input_type == "Enter Job Description":
                jd_input = st.text_area("Enter Job Description:")
                submit_button = st.button("Submit JD")

                if submit_button:
                    try:
                        data = clean_text(jd_input)
                        portfolio.load_portfolio()  # Call the method on the instance
                        jobs = chain.extract_jobs(data)
                        generate_emails(jobs, portfolio, chain)  # Call the generate_emails function
                    except Exception as e:
                        st.error(f"An error occurred: {e}")

        # Define the generate_emails function before it's called
        def generate_emails(jobs, portfolio, llm):
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')

        # Call the create_streamlit_app function
        create_streamlit_app(chain, portfolio, clean_text)
