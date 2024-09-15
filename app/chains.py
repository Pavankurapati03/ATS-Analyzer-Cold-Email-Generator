import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
    """
    ### JOB DESCRIPTION:
    {job_description}

    ### INSTRUCTION:
    You are writing this email on behalf of Kurapati Pavankumar, who is currently pursuing his final year of B.Tech in Artificial Intelligence and Data Science. He has completed internships in the fields of ML, AI, Generative AI, Data Science, and Data Analytics, and has worked on several projects in these domains.
    
    Write a professional cold email introducing Kurapati's skills, experience, and interest in the job described above. Make sure to highlight his **relevant project work, internships, and skills based on the job description** (only the skills that are relevant to the JD should be mentioned). The email should also include his contact information, LinkedIn, and GitHub profile for further reference. Keep the tone formal and concise.

    At the end of the email, include:
    
    - Best regards,
    - Kurapati Pavankumar
    - Email: pavankurapati0105@gmail.com
    - Mobile: 720****326
    - LinkedIn: https://www.linkedin.com/in/pavankumar-kurapati/
    - GitHub: https://github.com/Pavankurapati03
    
    Additionally, mention that Kurapati has attached his resume to the email.

    ### SKILL SET:
    Kurapati has a broad skill set in the following areas:
    - Languages: Python, HTML, CSS
    - Databases: SQL, Vector Databases
    - Tools & Libraries: Scikit-Learn, NLTK, Pandas, Numpy, Matplotlib, Seaborn, LangChain, Flask, Power BI, MS-Excel, Power Query, BeautifulSoup, Selenium, Streamlit, Dialogflow, Git, OpenCV
    - Frameworks: Tensorflow, Keras, Pytorch, Bootstrap, Transformers
    - Cloud Platforms: AWS
    - Areas: Model Building and Optimization, Fine-tuning, Generative AI, Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Research, Machine Learning, Deep Learning, Predictive Analytics, Data Analytics, Statistical Analysis, NLP, Web Scraping, GAN, ETL
    - Soft Skills: Time management, teamwork, Problem-solving, Attention to detail, Communication, Adaptability, Collaboration

    Make sure to mention only the most relevant skills for the job based on the job description.
    
    ### EMAIL (NO PREAMBLE):
    """
)

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
    
    