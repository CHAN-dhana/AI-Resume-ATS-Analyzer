from django import forms

class ResumeForm(forms.Form):
    resume = forms.FileField(label="Upload Resume")
    job_description = forms.CharField(
        widget=forms.Textarea,
        label="Job Description",
        required=False
    )