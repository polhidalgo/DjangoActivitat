from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('students', views.students_view, name='students'),
    path('students/<int:student_id>/', views.student_detail_view, name='student_detail'),
    path('teachers', views.teachers_view, name='teachers'),
    path('teachers/<int:teacher_id>/', views.teacher_detail_view, name='teacher_detail'),
    path('students/add', views.add_student, name='add_student'),
    path('teachers/add', views.add_teacher, name='add_teacher')
]