from django.urls import path
from . import views

urlpatterns = [
    path('students', views.students_view, name='students'),

    path('teachers', views.teachers_view, name='teachers')
]