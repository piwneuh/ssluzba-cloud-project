from django.shortcuts import render, redirect
from .forms import ProfessorRegistrationForm

# Create your views here.
def professor_registration(request):
    if request.method == 'POST':
        form = ProfessorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProfessorRegistrationForm()
    return render(request, 'professor_registration.html', {'form:form'})