from django import forms

from app.models import Usuari


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrerForm(forms.ModelForm):
    class Meta:
        model = Usuari
        fields = '__all__'
