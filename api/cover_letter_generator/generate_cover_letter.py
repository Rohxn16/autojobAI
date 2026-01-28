from fastapi import APIRouter
from modules.agentic_modules.cover_letter_writer import cover_letter_writer

router = APIRouter()

@router.post('/generate-cover-letter')
def generate_cover_letter():

    response = cover_letter_writer(
        mail='hivyr@protonmail.com',
        jd="""
        Machine Learning Intern



Company: Inficore Soft

Location: Remote

Internship Type: Full-Time

Duration: 1–3 Months

Stipend: ₹15,000 per month



⸻



About the Internship



Inficore Soft is seeking a motivated and analytical Machine Learning Intern to work on real-world data-driven and AI-based projects. This internship is ideal for candidates who want practical exposure to machine learning algorithms, model development, and applied analytics in a professional remote environment.



⸻



Key Responsibilities

• Assist in building, training, and evaluating machine learning models

• Work with structured and unstructured datasets

• Perform data preprocessing, feature engineering, and data cleaning

• Implement machine learning algorithms such as regression, classification, and clustering

• Analyze model performance and optimize results

• Collaborate with data scientists and developers on live projects

• Document models, workflows, and results



⸻



Eligibility Criteria

• Currently pursuing or recently completed a degree in Computer Science, Data Science, AI, Statistics, or a related field

• Strong understanding of Python programming

• Basic knowledge of machine learning concepts and algorithms

• Familiarity with libraries such as NumPy, Pandas, Scikit-learn, or TensorFlow is a plus

• Understanding of data analysis and statistics fundamentals

• Exposure to SQL or data visualization tools is an advantage

• Strong analytical and problem-solving skills

• Ability to work independently in a remote environment



⸻



What We Offer

• Hands-on experience with real-world machine learning projects

• Mentorship from experienced AI and data professionals

• Exposure to industry-standard ML tools and workflows

• Internship Certificate upon successful completion

• Opportunity for future full-time roles based on performance
"""
    )

    return {'cover_letter': response}
