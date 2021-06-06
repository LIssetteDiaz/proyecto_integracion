from django.shortcuts import render
from .models import Producto

# Create your views here.

def Inicio(request):
    return render(request, "src/inicio.html")


def GaleriaInstrumentos(request):

    instrumentos = Producto.objects.all()
    
    context ={
        'instrumentos':instrumentos
    }
    return render(request, "src/instrumentos.html",context)


def carrito(request):
    return render(request, "src/carrito.html")


