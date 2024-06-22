from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .forms import CourseForm, ProjectForm, StudentForm
from .models import Course, Project, Student


def index(request):
    courses = Course.objects.all()
    projects = Project.objects.all()
    students = Student.objects.all()
    return render(request, 'student_course_registration_app/index.html', { 'courses': courses,'projects': projects,'students':students})


def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'student_course_registration_app/register_student.html', {'form': form})
    
def register_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = CourseForm()
    return render(request, 'student_course_registration_app/register_course.html', {'form': form})
    
def student_list(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.students.all()
    return render(request, 'student_course_registration_app/student_list.html', {'students': students, 'course': course})

def register_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request, 'student_course_registration_app/register_project.html', {'form': form})

class StudentListView(ListView):
    model = Student
    template_name = 'student_course_registration_app/stu_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_course_registration_app/student_detail.html'
    context_object_name = 'student'
