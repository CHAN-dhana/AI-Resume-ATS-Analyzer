import re


def check_sections(resume_text):

    text = resume_text.lower()

    sections = {

        "Contact Info": False,
        "Skills": False,
        "Experience": False,
        "Education": False,
        "Projects": False,
        "Certificates": False,
        "Achievements": False,
        "Languages": False,
        "Interests": False

    }

    # Contact Information
    if re.search(r'email|phone|mobile', text):
        sections["Contact Info"] = True

    # Resume Sections
    if "skills" in text:
        sections["Skills"] = True

    if "experience" in text:
        sections["Experience"] = True

    if "education" in text:
        sections["Education"] = True

    if "project" in text or "projects" in text:
        sections["Projects"] = True

    if any(word in text for word in [
    "certificate",
    "certificates",
    "certification",
    "certifications",
    "course",
    "courses",
    "training"]):
        sections["Certificates"] = True

    if "achievement" in text or "achievements" in text:
        sections["Achievements"] = True

    if "language" in text or "languages" in text:
        sections["Languages"] = True

    if "interest" in text or "interests" in text:
        sections["Interests"] = True

    return sections