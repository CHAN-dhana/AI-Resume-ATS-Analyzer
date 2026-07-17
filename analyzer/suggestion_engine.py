def generate_suggestions(missing_skills, sections, score):

    suggestions = []

    # Skill based suggestions
    if missing_skills:
        suggestions.append(
            "Add these skills to your resume: " + ", ".join(missing_skills)
        )

    # Section suggestions
    if not sections["Projects"]:
        suggestions.append("Add a Projects section with your best work.")

    if not sections["Skills"]:
        suggestions.append("Add a Skills section highlighting technical skills.")

    if not sections["Experience"]:
        suggestions.append("Add work experience or internship details.")

    if not sections["Education"]:
        suggestions.append("Add your education details.")

    if not sections["Certificates"]:
        suggestions.append("Add Certificates / Certifications / Courses / Training section.")

    # Score based suggestions
    if score < 50:
        suggestions.append("Your resume needs major improvements to pass ATS systems.")

    elif score < 70:
        suggestions.append("Your resume is decent but can be improved with better keywords.")

    else:
        suggestions.append("Good resume! Try adding more achievements to stand out.")

    return suggestions