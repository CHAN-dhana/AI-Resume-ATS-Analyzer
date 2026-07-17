from django.urls import path
from .views import home, resume_builder

urlpatterns = [
    path('', home, name='home'),
    path("resume-builder/", resume_builder, name="resume_builder")
]