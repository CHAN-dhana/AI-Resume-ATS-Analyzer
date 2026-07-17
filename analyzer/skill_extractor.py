import re

# --------------------------
# SKILLS DATABASE
# --------------------------
SKILLS_DB = [
    "python", "java", "c++", "c", "javascript", "html", "css",
    "django", "flask", "react", "angular", "vue",
    "sql", "mysql", "postgresql", "mongodb", "sqlite",
    "aws", "azure", "gcp",
    "docker", "kubernetes", "jenkins", "git",
    "machine learning", "deep learning", "nlp", "ai",
    "tensorflow", "pytorch", "scikit-learn"
]


# --------------------------
# SKILL EXTRACTOR FUNCTION
# --------------------------
def extract_skills(text):

    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.append(skill)

    return list(set(found_skills))