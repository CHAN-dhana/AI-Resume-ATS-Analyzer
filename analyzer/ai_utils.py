import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

def analyze_resume(resume_text, job_description):
    model = genai.GenerativeModel("gemini-1.5-flash-latest")

    prompt = f"""
    You are an ATS Resume Analyzer.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Return:
    - ATS Score out of 100
    - Matching Skills
    - Missing Skills
    - Suggestions
    """

    response = model.generate_content(prompt)
    return response.text