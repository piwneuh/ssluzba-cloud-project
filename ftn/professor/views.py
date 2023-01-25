from django.shortcuts import render, redirect
from .forms import ProfessorRegistrationForm
from .models import Professor

# Create your views here.
def home(request):
    return render(request, 'home.html')
    
def professor_table(request):
    professors = Professor.objects.all()
    return render(request, 'professor_table.html', {'professors': professors})

def professor_registration(request):
    if request.method == 'POST':
        form = ProfessorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professor-table')
    else:
        form = ProfessorRegistrationForm()
    return render(request, 'professor_registration.html', {'form':form})