def explain_score(resume_text, score, matched, missing, sections):

    explanation = []

    text = resume_text.lower()

    # -------------------------
    # SCORE INTERPRETATION
    # -------------------------
    if score < 50:
        explanation.append("❌ Resume is weak and needs major improvements.")
    elif score < 75:
        explanation.append("⚠ Resume is average but can be improved.")
    else:
        explanation.append("✅ Strong resume with good structure.")

    # -------------------------
    # MISSING SECTIONS
    # -------------------------
    if "skills" not in text:
        explanation.append("❌ Missing Skills section (very important for ATS).")

    if "experience" not in text:
        explanation.append("❌ Missing Experience section.")

    if "education" not in text:
        explanation.append("❌ Missing Education section.")

    # -------------------------
    # KEYWORD MATCH INSIGHT
    # -------------------------
    if len(missing) > len(matched):
        explanation.append("⚠ Resume does not match job description well.")

    if len(matched) > len(missing):
        explanation.append("✅ Good keyword match with job description.")

    # -------------------------
    # FORMAT INSIGHT
    # -------------------------
    if "•" not in resume_text and "-" not in resume_text:
        explanation.append("⚠ Improve formatting using bullet points.")

    return explanation