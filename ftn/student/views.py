from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from .models import Student

# Create your views here.
def student_table(request):
    students = Student.objects.all()
    return render(request, 'student_table.html', {'students': students})

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-table')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_registration.html', {'form': form})