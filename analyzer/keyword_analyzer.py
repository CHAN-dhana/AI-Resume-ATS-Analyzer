import re

STOP_WORDS = {
    "the", "and", "for", "with", "that", "this", "have", "has",
    "are", "will", "from", "your", "you", "our", "their",
    "into", "using", "used", "need", "required", "requirements",
    "candidate", "experience", "knowledge", "ability", "good",
    "strong", "excellent", "skills", "skill", "years", "year",
    "job", "role", "work", "team", "company", "must", "should",
    "preferred", "responsible"
}


def keyword_density(resume_text, job_description=""):

    # No Job Description -> No keyword analysis
    if not job_description.strip():
        return None

    resume = resume_text.lower()
    jd = job_description.lower()

    # Extract words
    jd_words = re.findall(r"[a-zA-Z][a-zA-Z+#.-]*", jd)

    # Remove stop words and duplicates
    keywords = []

    for word in jd_words:
        if len(word) > 2 and word not in STOP_WORDS:
            if word not in keywords:
                keywords.append(word)

    matched = []
    missing = []

    for word in keywords:
        if word in resume:
            matched.append(word)
        else:
            missing.append(word)

    percentage = 0

    if keywords:
        percentage = round((len(matched) / len(keywords)) * 100, 2)

    return {
        "matched": matched,
        "missing": missing,
        "percentage": percentage
    }