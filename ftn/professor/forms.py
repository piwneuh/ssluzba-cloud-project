from django import forms
from .models import Professor

class ProfessorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['first_name', 'last_name', 'email']