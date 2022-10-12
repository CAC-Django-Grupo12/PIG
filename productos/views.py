from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "index.html")

def producto(request, id):
    return render(request, "producto.html", {"id": id, "nombre": "primer producto"})

def about(request):
    return HttpResponse("Acerca de")