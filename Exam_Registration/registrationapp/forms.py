from django import forms
from .models import Exam, StudentRegistration

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'description', 'date', 'duration']


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ['user', 'exam']
