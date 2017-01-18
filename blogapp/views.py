from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import FormView

from .models import Entrada

# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    model = Entrada

class FormView(ListView):
    template_name = 'formulario.html'
    model = Entrada
