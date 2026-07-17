from django import forms


class ResumeBuilderForm(forms.Form):

    # PERSONAL INFO (mandatory)
    name = forms.CharField(label="Full Name", required=True)

    email = forms.EmailField(label="Email", required=True)

    phone = forms.CharField(label="Phone", required=True)

    # OPTIONAL CONTACT LINKS
    github = forms.CharField(label="GitHub", required=False)

    linkedin = forms.CharField(label="LinkedIn", required=False)

    # EDUCATION (optional)
    college_name = forms.CharField(label="College Name", required=False)

    degree = forms.CharField(label="Degree", required=False)

    passing_year = forms.IntegerField(label="Passing Year", required=False)

    percentage = forms.FloatField(
        label="Percentage / CGPA",
        required=False
    )

    # SKILLS (optional)
    skills = forms.CharField(
        widget=forms.Textarea,
        label="Skills",
        required=False
    )

    # EXPERIENCE (optional)
    experience = forms.CharField(
        widget=forms.Textarea,
        label="Experience",
        required=False
    )

    # PROJECTS (optional)
    projects = forms.CharField(
        widget=forms.Textarea,
        label="Projects",
        required=False
    )

    # CERTIFICATES (optional)
    certificates = forms.CharField(
        widget=forms.Textarea,
        label="Certificates",
        required=False
    )

    # ACHIEVEMENTS (optional)
    achievements = forms.CharField(
        widget=forms.Textarea,
        label="Achievements",
        required=False
    )

    # TEMPLATE SELECTION
    template = forms.ChoiceField(

        choices=[
            ("classic", "Classic ATS"),
            ("modern", "Modern Developer"),
            ("minimal", "Minimal Professional")
        ],

        label="Select Resume Template",
        required=False
    )