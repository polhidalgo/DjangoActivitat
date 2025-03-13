from django.db import models
from django import forms
from django.contrib.postgres.fields import ArrayField


class Teacher(models.Model):
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100, blank=True)
    correu = models.EmailField(unique=True)
    # El professor pot impartir diversos cursos (llista de codi de curs, ex: 'DAW2B', 'DAW2A')
    curs = ArrayField(
        base_field=models.CharField(max_length=10),
        blank=True,
        default=list,
        help_text="Llistat de cursos que imparteix"
    )
    tutor = models.BooleanField(default=False)
    # Llista de mòduls que imparteix
    moduls = ArrayField(
        base_field=models.CharField(max_length=10),
        blank=True,
        default=list,
        help_text="Llistat de mòduls"
    )

    def __str__(self):
        return f"{self.nom} {self.cognom1} ({'Tutor' if self.tutor else 'No tutor'})"


class Student(models.Model):
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100, blank=True)
    correu = models.EmailField(unique=True)
    # En el cas dels alumnes, 'curs' es guarda com a cadena (per exemple, 'DAW2A')
    curs = models.CharField(
        max_length=10,
        help_text="Curs en què està matriculat l'alumne"
    )
    # Llista de mòduls matriculats
    moduls = ArrayField(
        base_field=models.CharField(max_length=10),
        blank=True,
        default=list,
        help_text="Llistat de mòduls matriculats"
    )

    def __str__(self):
        return f"{self.nom} {self.cognom1} ({self.curs})"



