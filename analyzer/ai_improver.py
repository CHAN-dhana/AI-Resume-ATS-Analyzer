import os
import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

def improve_resume(text):
    model = genai.GenerativeModel("gemini-1.5-flash-latest")

    try:
        response = model.generate_content(
            f"""
You are a resume expert AI.

Analyze and improve the resume below:

{text}

Return clearly in this format:
- Improvements
- Suggestions
"""
        )

        return response.text, []

    except Exception as e:
        return f"Error: {str(e)}", []