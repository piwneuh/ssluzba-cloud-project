from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm

# Create your views here.
def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_registration.html', {'form': form})