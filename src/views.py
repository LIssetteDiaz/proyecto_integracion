from django.shortcuts import render
from .models import Instrumentos

# Create your views here.

def Inicio(request):
    return render(request, "src/inicio.html")

def GaleriaInstrumentos(request):

    instrumentos = Instrumentos.objects.all()
    
    context ={
        'instrumentos':instrumentos
    }
    return render(request, "src/instrumentos.html",context)