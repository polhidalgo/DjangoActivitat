from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Usuari
from .forms import LoginForm, RegistrerForm


# Create your views here.
def login_view(request):
    if "usuari_id" in request.session:
        return redirect("inici")

    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]

        try:
            usuari = Usuari.objects.get(email=email)
            if check_password(password, usuari.password):
                request.session["usuari_id"] = usuari.id
                return redirect("inici")
            else:
                messages.error(request, "Contrasenya no correcte")
        except Usuari.DoesNotExist:
            messages.error(request, "Usuari no existeix")

    return render(request, "login.html", {"form": form})

# Vista de registre
def register_view(request):
    if "usuari_id" in request.session:
        return redirect("inici")

    form = RegistrerForm()

    if request.method == 'POST':
        form = RegistrerForm(request.POST)
        if form.is_valid():
            usuari = form.save(commit=False)
            usuari.password = make_password(form.cleaned_data["password"])
            usuari.save()
        messages.success(request, "Registre completat! Ara pots iniciar sessió.")
        return redirect("login")

    return render(request, "register.html", {"form": form})

# Vista d'inici de sessió
def inici_view(request):
    usuari_id = request.session.get("usuari_id")
    if not usuari_id:
        return redirect("login")

    usuari = Usuari.objects.get(id=usuari_id)
    return render(request, "inici.html", {"nom": usuari.nom})

# Vista de logout
def logout_view(request):
    request.session.flush()
    return redirect("login")