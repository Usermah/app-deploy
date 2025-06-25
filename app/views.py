from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
def second(request):
    return HttpResponse("Hello, this is the second one")

def pass_data(request):
    some_data = { 
        "name" : "John Doe",
        "age" : "55"
    }
    return render(request, 'pass_data.html', context=some_data)

def student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Datails added successfully")
            return redirect('student')
    
    context = {}
    context['form']=form

    return render(request, 'student.html', context)

def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'student_list.html', context)

def form(request):
    return render(request, 'form.html')

def about(request):
    return render(request, 'about.html')


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)