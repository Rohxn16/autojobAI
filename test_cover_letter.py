
from modules.agent.cover_letter_writer.cover_letter_writer import cover_letter_writer

jd = """
Job Title: Senior Software Engineer
Company: Tech Corp
Responsibilities:
- Build scalable web applications using Python and React.
- Design database schemas.
- Collaborate with the product team.
Requirements:
- 5+ years of experience in Software Engineering.
- Proficiency in Python, Django, and React.
- Experience with cloud platforms like AWS.
"""

email = "rohxn16@gmail.com"

print("Starting Cover Letter Generation Test...")
try:
    output_path = cover_letter_writer(jd, email)
    print(f"Test Successful! File generated at: {output_path}")
except Exception as e:
    print(f"Test Failed with error: {e}")
