from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def cover_letter_writer(mail:str, jd:str):
    """
    Generates a "cover letter" mail to the addressed email id based on the given resume addressing
    the job description provided.
    """

    # getting resume data from the /uploads/resume.txt file
    with open('./uploads/resume.txt', 'r') as f:
        resume = f.read()

    llm = ChatOllama(
        model='gemma3:12b',
        temperature=0.2,
        max_tokens=1000,
        top_p=0.9,
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are an expert Career Strategist. Write a high-conversion, professional email "
            "for the candidate based on the provided Resume and Job Description (JD). "
            "\n\nSTRICT RULES:\n"
            "1. NO PLACEHOLDERS: Extract the candidate's name (Rohan Dey), skills, and company details "
            "directly from the context. If a detail is missing, write around it naturally.\n"
            "2. TONE: Professional, result-oriented, and concise. Avoid 'Dear Hiring Manager' if "
            "a name is available; otherwise, use a professional greeting.\n"
            "3. FOCUS: Highlight technical as well as soft skills. "
            "where relevant to the JD."
        )),
        ("user", (
            "Recipient Email: {mail_id}\n\n"
            "Job Description:\n{jd}\n\n"
            "Candidate Resume:\n{resume}\n\n"
            "Generate the ready-to-send email now:"
        ))
    ])

    chain = prompt | llm | StrOutputParser()

    try:
        response = chain.invoke({
            'mail_id': mail,
            'jd': jd,
            'resume': resume
        })
        return response
    except Exception as e:
        print(e)
        return f'Error in generating cover letter: {e}'