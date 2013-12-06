from django import forms
from django.db import models

# Create your models here.

class FormPersona(forms.Form):
	nombre = forms.URLField()

class Persona(models.Model):
	''' El URL de la pagina'''
	nombre = models.URLField()
