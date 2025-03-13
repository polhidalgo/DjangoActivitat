from django.shortcuts import render, redirect,get_object_or_404
from centre.models import Student, Teacher
from .forms import StudentForm, TeacherForm

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

def add_student(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')

    context = {'form': form}
    return render(request, 'centre/add_student.html', context)

def add_teacher(request):
    form = TeacherForm()

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')

    context = {'form': form}
    return render(request, 'centre/add_teacher.html', context)

def home_view(request):
    return render(request, 'centre/base.html')

def student_detail_view(request, student_id):

    student = get_object_or_404(Student, pk=student_id)
    context = {
        'title': f'Detalls de {student.nom} {student.cognom1}',
        'student': student,
    }
    return render(request, 'centre/student_detail.html', context)

def teacher_detail_view(request, teacher_id):

    teacher = get_object_or_404(Teacher, pk=teacher_id)
    context = {
        'title': f'Detalls de {teacher.nom} {teacher.cognom1}',
        'teacher': teacher,
    }
    return render(request, 'centre/teacher_detail.html', context)
