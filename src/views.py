from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render(request, "src/inicio.html")

def carrito(request):
    return render(request, "src/carrito.html")