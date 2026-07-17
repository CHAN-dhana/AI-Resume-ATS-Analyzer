from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas

from .ai_improver import improve_resume
from .forms import ResumeForm
from .resume_parser import extract_resume_text
from .ats_score import calculate_ats_score
from .skill_extractor import extract_skills
from .skill_matcher import match_skills
from .section_checker import check_sections
from .keyword_analyzer import keyword_density
from .suggestion_engine import generate_suggestions
from .resume_builder_forms import ResumeBuilderForm
from .score_explainer import explain_score
from .ats_score import (
    calculate_ats_score,
    structure_score,
    content_score,
    format_score,
)

# ----------------------------
# RESUME BUILDER
# ----------------------------
def resume_builder(request):

    form = ResumeBuilderForm()

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        github = request.POST.get("github")
        linkedin = request.POST.get("linkedin")
        objective = request.POST.get("objective")

        skills = [
             skill.strip()
             for skill in request.POST.getlist("skills[]")
             if skill.strip()
        ]
        companies = request.POST.getlist("company[]")
        roles = request.POST.getlist("role[]")
        durations = request.POST.getlist("duration[]")
        descriptions = request.POST.getlist("experience_detail[]")

        experience = []

        for i in range(len(companies)):
         if companies[i].strip() or roles[i].strip() or descriptions[i].strip():
            experience.append([
            companies[i],
            roles[i],
            durations[i],
            descriptions[i]
        ])
        college = request.POST.getlist("college_name[]")
        degree = request.POST.getlist("degree[]")
        year = request.POST.getlist("year[]")
        percentage = request.POST.getlist("percentage[]")

        project_name = request.POST.getlist("project_name[]")
        project_detail = request.POST.getlist("project_detail[]")
        project_link = request.POST.getlist("project_link[]")

        certificates = request.POST.getlist("certificates[]")
        achievements = request.POST.getlist("achievements[]")

        languages = request.POST.getlist("languages[]")
        interests = request.POST.getlist("interests[]")
        links = request.POST.getlist("links[]")

        education = list(zip(college, degree, year, percentage))        
        projects = list(zip(project_name, project_detail, project_link))
        company = request.POST.getlist("company[]")
        role = request.POST.getlist("role[]")
        duration = request.POST.getlist("duration[]")
        experience_detail = request.POST.getlist("experience_detail[]")

        experience = []

        for i in range(len(company)):
          if company[i].strip() or role[i].strip() or experience_detail[i].strip():

           experience.append([
            company[i],
            role[i],
            duration[i],
            experience_detail[i]
        ])
        # AI Improve (Gemini)
        resume_text = " ".join(skills) + " " + (objective or "")
        ai_suggestions, rewrites = improve_resume(resume_text)

        context = {
            "name": name,
            "email": email,
            "phone": phone,
            "github": github,
            "linkedin": linkedin,
            "objective": objective,
            "skills": skills,
            "experience": experience,
            "education": education,
            "projects": projects,
            "certificates": certificates,
            "achievements": achievements,
            "languages": languages,
            "interests": interests,
            "links": links,
            "ai_suggestions": ai_suggestions,
            "rewrites": rewrites
        }

        if "preview" in request.POST:
            return render(request, "resume_preview.html", context)

        # ----------------------------
        # PDF DOWNLOAD
        # ----------------------------
        if "download" in request.POST:

            response = HttpResponse(content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="resume.pdf"'

            p = canvas.Canvas(response)

            text = p.beginText(50, 800)
            text.setFont("Helvetica", 11)
            text.setLeading(16)

            text.setFont("Helvetica-Bold", 16)
            text.textLine(name)

            text.setFont("Helvetica", 11)

            contact = f"{email} | {phone}"

            if linkedin:
                contact += f" | {linkedin}"

            if github:
                contact += f" | {github}"

            text.textLine(contact)
            text.textLine("")

            if objective:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("OBJECTIVE")
                text.setFont("Helvetica", 11)
                text.textLine(objective)
                text.textLine("")

            if skills:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("SKILLS")

                for s in skills:
                    if s:
                        text.textLine(f"• {s}")

                text.textLine("")

            if experience:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("EXPERIENCE")

                for c, r, d, desc in experience:

                    if not c and not r and not desc:
                        continue

                    if r:
                        text.setFont("Helvetica-Bold", 11)
                        text.textLine(r)

                    text.setFont("Helvetica", 11)

                    if c:
                        text.textLine(c)

                    if d:
                        text.textLine(d)

                    if desc:
                        text.textLine(desc)

                    text.textLine("")

            if education:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("EDUCATION")

                for c, d, y, pct in education:                  
                    if c:
                        text.textLine(c)

                    if d:
                        text.textLine(f"{d} - {y}")

                    if pct:
                        if "." in pct:
                             text.textLine(f"CGPA: {pct}")
                        else:
                             text.textLine(f"Percentage: {pct}")
                    text.textLine("")

            if projects:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("PROJECTS")

                for n, d, l in projects:

                    if not n and not d and not l:
                        continue

                    if n:
                        text.setFont("Helvetica-Bold", 11)
                        text.textLine(n)

                    text.setFont("Helvetica", 11)

                    if d:
                        text.textLine(d)

                    if l:
                        text.textLine(l)

                    text.textLine("")

            if certificates:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("CERTIFICATES")

                for c in certificates:
                    if c:
                        text.textLine(f"• {c}")

                text.textLine("")

            if achievements:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("ACHIEVEMENTS")

                for a in achievements:
                    if a:
                        text.textLine(f"• {a}")

                text.textLine("")

            p.drawText(text)
            p.save()

            return response

    return render(request, "resume_builder.html", {"form": form})


# ----------------------------
# ATS ANALYZER HOME
# ----------------------------
def home(request):

    score = None
    skills = None
    matched = []
    missing = []
    sections = None
    keywords = None
    suggestions = None
    ai_suggestions = []
    rewrites = []
    match_percent = 0
    strength = ""
    explanation = ""   # ✅ IMPORTANT FIX

    if request.method == "POST":

        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():

            resume_file = request.FILES["resume"]
            job_description = form.cleaned_data["job_description"]

            resume_text = extract_resume_text(resume_file)

            # ----------------------------
            # ANALYSIS MODULES
            skills = extract_skills(resume_text)
            sections = check_sections(resume_text)

            keywords = None  # default
            matched = []
            missing = []

            if job_description.strip():

              keywords = keyword_density(resume_text, job_description)

              matched, missing = match_skills(resume_text, job_description)
              total = len(matched) + len(missing)

              if total > 0:
                match_percent = round((len(matched) / total) * 100, 2)
              else:
               match_percent = 0

              resume_quality = calculate_ats_score(resume_text, "")
 
              score = round(
                 resume_quality * 0.60 +
                 match_percent * 0.40,
                 2
              )

            else:

                 score = calculate_ats_score(resume_text, "")
            # ----------------------------
            # AI MODULE
            # ----------------------------
            ai_suggestions, rewrites = improve_resume(resume_text)

            
            # ----------------------------
            # SUGGESTIONS
            # ----------------------------
            suggestions = generate_suggestions(missing, sections, score)

            # ----------------------------
            # SCORE EXPLANATION (NOW CORRECT ORDER)
            # ----------------------------
            try:
              explanation = explain_score(
                resume_text,
                score,
                matched,
                missing,
                sections
            )
            except:
               explanation = "Score explanation not available."

            # ----------------------------
            # RESUME STRENGTH
            # ----------------------------
            # Resume Strength

            if job_description.strip():

              if match_percent >= 90 and score >= 70:
                 strength = "Strong Resume"

              elif match_percent >= 70 and score >= 60:
                 strength = "Average Resume"

              else:
                 strength = "Weak Resume"

            else:

              if score >= 80:
                 strength = "Strong Resume"

              elif score >= 65:
                 strength = "Average Resume"

              else:
                strength = "Weak Resume"

    else:
        form = ResumeForm()

    return render(request, "home.html", {
        "form": form,
        "score": score,
        "skills": skills,
        "matched": matched,
        "missing": missing,
        "sections": sections,
        "keywords": keywords,
        "suggestions": suggestions,
        "ai_suggestions": ai_suggestions,
        "rewrites": rewrites,
        "match_percent": match_percent,
        "strength": strength,
        "explanation": explanation
    })