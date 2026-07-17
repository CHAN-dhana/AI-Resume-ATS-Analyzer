# AI Resume ATS Analyzer

An AI-powered Resume ATS Analyzer and Resume Builder built with Django.
This project helps job seekers analyze their resumes, check ATS compatibility, generate AI-powered improvement suggestions, and create professional ATS-friendly resumes.

## Project Overview

AI Resume ATS Analyzer is a web application designed to evaluate resumes against modern Applicant Tracking Systems (ATS). It analyzes resume content, extracts technical skills, compares resumes with job descriptions, calculates ATS compatibility scores, and provides personalized improvement suggestions using Google Gemini AI.

The system also includes a Resume Builder that enables users to create, preview, and download professional ATS-friendly resumes in PDF format.

## Key Features

* AI-powered Resume Analysis using Google Gemini
* Resume ATS Score Calculation
* Resume Parsing and Text Extraction
* Skill Extraction from Resume
* Skill Matching with Job Description
* Keyword Density Analysis
* Missing Skills Identification
* Resume Quality Analysis
* AI-powered Resume Improvement Suggestions
* Resume Section Detection (Skills, Education, Experience, Projects, Certificates, Achievements, Languages, and Interests)
* Smart Certificate Detection (Supports Certificates, Certifications, Courses, and Training)
* ATS-friendly Resume Builder
* Multiple Resume Templates
* PDF Resume Generation using ReportLab
* Responsive and User-friendly Web Interface

## Tech Stack

### Backend

* Python
* Django

### AI & Machine Learning

* Google Gemini API
* Scikit-learn (TF-IDF & Cosine Similarity)

### Libraries

* ReportLab (PDF Generation)

### Frontend

* HTML
* CSS
* Bootstrap
* Django Templates

### Database

* SQLite

## Project Structure

ai_resume_ats
│
├── ai_resume_ats (Django project settings)
├── analyzer (Main application logic)
│ ├── ats_score.py
│ ├── ai_improver.py
│ ├── skill_extractor.py
│ ├── keyword_analyzer.py
│ ├── resume_parser.py
│ ├── suggestion_engine.py
│ ├── section_checker.py
│ └── views.py
│
├── templates
│ ├── home.html
│ ├── resume_builder.html
│ └── resume_preview.html
│
├── manage.py
├── requirements.txt

## Installation

Clone the repository

git clone git clone https://github.com/CHAN-dhana/AI-Resume-ATS-Analyzer.git

Navigate to the project directory

cd your-repository

Create virtual environment

python -m venv venv

Activate environment

Windows:

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run the Django server

python manage.py runserver

Open in browser

http://127.0.0.1:8000/

## How It Works

1. Upload your resume or create one using the Resume Builder.
2. Enter a job description (optional).
3. The system extracts resume content.
4. It analyzes resume sections, keywords, and technical skills.
5. ATS compatibility score is calculated.
6. AI generates personalized resume improvement suggestions.
7. Users can preview and download ATS-friendly PDF resumes.

## Future Improvements

* User Authentication and Profile Management
* Resume History and Version Tracking
* Machine Learning-based ATS Ranking
* Job Recommendation System
* AI-powered Resume Rewriting
* Additional Resume Templates
* Cloud Deployment

## Author

Chandana S

GitHub: https://github.com/CHAN-dhana

## License

This project is for educational and learning purposes.
