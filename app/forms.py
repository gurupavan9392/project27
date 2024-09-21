from django import forms
from app.models import *



class StudentFV(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'