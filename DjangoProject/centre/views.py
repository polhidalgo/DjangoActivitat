from django.shortcuts import render
from centre.models import Student, Teacher

def students_view(request):
    students = Student.objects.all()
    context = {
        'title': 'Informació Alumnat DAW2A',
        'students': students
    }
    return render(request, 'centre/students.html', context)

def teachers_view(request):
    teachers = Teacher.objects.all()
    context = {
        'title': 'Informació Professorat TIC Barcelona',
        'teachers': teachers
    }
    return render(request, 'centre/teachers.html', context)
