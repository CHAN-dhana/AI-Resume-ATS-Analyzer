from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_ats_score(resume_text, job_description=""):

    structure = structure_score(resume_text)
    content = content_score(resume_text)
    formatting = format_score(resume_text)

    # ----------------------------
    # NO JOB DESCRIPTION
    # ----------------------------
    if not job_description.strip():

        final_score = (
            structure * 0.35 +
            content * 0.45 +
            formatting * 0.20
        )

        return round(final_score, 2)

    # ----------------------------
    # JOB DESCRIPTION AVAILABLE
    # ----------------------------

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

    keyword_score = similarity * 100

    final_score = (
        structure * 0.20 +
        content * 0.30 +
        formatting * 0.10 +
        keyword_score * 0.40
    )

    return round(final_score, 2)
# --------------------------------
# STRUCTURE SCORE
# --------------------------------

def structure_score(resume_text):

    text = resume_text.lower()

    score = 0

    required = [
        "education",
        "experience",
        "skills",
        "project"
    ]

    optional = [
        "certificate",
        "certification",
        "achievement",
        "language",
        "interest"
    ]

    for section in required:
        if section in text:
            score += 20

    for section in optional:
        if section in text:
            score += 4

    return min(score, 100)

# --------------------------------
# CONTENT SCORE
# --------------------------------

def content_score(resume_text):

    text = resume_text.lower()

    technical_skills = [
        "python","java","c","c++","html","css","javascript",
        "react","angular","vue","django","flask",
        "mysql","postgresql","sqlite","mongodb",
        "git","github","docker","kubernetes",
        "aws","azure","gcp",
        "tensorflow","pytorch",
        "machine learning","deep learning",
        "nlp","llm","ai"
    ]

    count = 0

    for skill in technical_skills:
        if skill in text:
            count += 1

    if count >= 12:
        return 100
    elif count >= 10:
        return 90
    elif count >= 8:
        return 80
    elif count >= 6:
        return 70
    elif count >= 4:
        return 60
    elif count >= 2:
        return 50
    else:
        return 35

# --------------------------------
# FORMAT SCORE
# --------------------------------

def format_score(resume_text):

    score = 50

    if len(resume_text.split()) > 250:
        score += 15

    if "\n" in resume_text:
        score += 10

    if "@" in resume_text:
        score += 10

    if any(char.isdigit() for char in resume_text):
        score += 10

    if "•" in resume_text or "-" in resume_text:
        score += 5

    return min(score, 100)