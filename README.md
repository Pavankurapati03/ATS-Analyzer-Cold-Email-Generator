
# **ATS Analyzer & Cold Email Generator**

## **Table of Contents**
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [Usage](#usage)
  - [Landing Page](#landing-page)
  - [ATS Analyzer](#ats-analyzer)
  - [Cold Email Generator](#cold-email-generator)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Credits](#credits)

---

## **Project Overview**

This **Streamlit-based web application** combines two essential functionalities into one integrated project:
1. **ATS Analyzer**: Helps users analyze their resumes against job descriptions using **Google Gemini**. It highlights strengths, weaknesses, missing keywords, and provides a percentage match between the resume and the job description.
2. **Cold Email Generator**: Automatically generates personalized cold emails for job applications or networking using **Groq's LLaMA 3.1**.

This project is designed for AI/ML enthusiasts and professionals looking to enhance their job applications with AI-driven resume optimization and cold email generation.

---

## **Key Features**
- **Landing Page**: An introductory page with a quick overview of the available functionalities.
- **ATS Analyzer**:
  - Upload a PDF resume and compare it with a job description.
  - Get feedback on your resume, including strengths, weaknesses, missing keywords, and percentage match.
  - Uses **Google Gemini** for intelligent insights.
- **Cold Email Generator**:
  - Generate cold emails for job applications or outreach based on a job description or URL.
  - Leverages **Groq's LLaMA 3.1** for NLP-based email generation.

---

## **How It Works**

### ATS Analyzer:
- Upload a **PDF resume** and provide a **job description**.
- The system analyzes the resume using **Google Gemini** to identify missing keywords, provide feedback on skills, and offer suggestions for improvement.
- It also provides a **percentage match** with the job description.

### Cold Email Generator:
- Input a **job description** or a **URL** (such as a company page).
- The system analyzes the content and generates a personalized cold email using **Groq's LLaMA 3.1**.
- The email includes links to the portfolio and highlights relevant skills for the role.

---

## **Prerequisites**

Before setting up and running the project, ensure you have the following installed:

- Python 3.8 or higher
- Streamlit (`pip install streamlit`)
- Google Generative AI SDK (`pip install google-generativeai`)
- PDF processing library (such as `pdfplumber`)
- Environment variable manager (`python-dotenv`)
- LangChain components (`pip install langchain_community`)
- Git for version control

You'll also need:
- A **Google API Key** for **Google Gemini**.
- A **Groq's LLaMA API key** for the Cold Email Generator (optional, if using a local setup).

---

## **Installation Guide**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/integrated-proj.git
   cd integrated-proj
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the required Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory of the project.
   - Add your **Google API Key** for Google Gemini in the `.env` file:
     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```

5. **Run the App**:
   Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## **Usage**

### **Landing Page**
Once the app is launched, you'll see the **landing page** with a brief description of the two functionalities (ATS Analyzer and Cold Email Generator). Click on the **"Get Started"** button to navigate to the task selection page.

### **ATS Analyzer**

1. **Input the Job Description**: Paste the job description for the position you're interested in.
2. **Upload Resume**: Upload your resume in **PDF format**.
3. **Select Actions**:
   - **Tell Me About the Resume**: Get feedback on your resume's alignment with the job description.
   - **How Can I Improve My Skills?**: Get personalized suggestions for skill improvement.
   - **What are the Missing Keywords?**: Discover which keywords are missing from your resume.
   - **Percentage Match**: See the overall percentage match between the resume and the job description.

### **Cold Email Generator**

1. **Choose Input Method**:
   - Enter a **URL** (for example, a job listing or company page).
   - Or, paste the **Job Description** directly.
2. The system will generate a professional cold email, which you can copy and use for your applications.

---

## **Technologies Used**

- **Streamlit**: The main framework for creating the web app.
- **Google Gemini API**: Used for analyzing resumes and generating insights in the ATS Analyzer.
- **Groq's LLaMA 3.1**: NLP model for generating cold emails.
- **LangChain**: Framework for integrating multiple components and tasks.
- **pdfplumber**: For parsing PDF resumes.
- **dotenv**: For environment variable management.

---

## **Project Structure**

```
integrated-proj/
│
├── chains/
│   └── chain.py               # Handles Cold Email generation logic
├── portfolio/
│   └── portfolio.py           # Portfolio-related functions
├── utils/
│   └── utils.py               # Helper functions (e.g., clean_text)
├── .env                       # Contains API keys (not included in the repo)
├── app.py                     # Main Streamlit app
├── README.md                  # Project documentation (this file)
├── requirements.txt           # Python dependencies
└── ...
```

---

## **Future Improvements**

- **Expand Language Support**: Add multi-language support for analyzing resumes and generating emails in different languages.
- **Custom Models**: Allow users to upload custom LLM models for email generation or resume analysis.
- **Advanced Resume Parsing**: Implement more advanced resume parsing features, like extracting structured information (e.g., education, experience, skills).

---

## **Credits**

This project was built by [Pavankumar Kurapati](https://www.linkedin.com/in/pavankumar-kurapati/).

For any questions or contributions, feel free to reach out on LinkedIn or open a GitHub issue.

---

Feel free to customize the README file further to suit your needs!
