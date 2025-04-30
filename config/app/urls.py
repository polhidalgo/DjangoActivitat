from django.urls import path
from .views import login_view, register_view, inici_view, logout_view

urlpatterns = [
    path('', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('inici/', inici_view, name="inici"),
    path('logout/', logout_view, name="logout"),
]