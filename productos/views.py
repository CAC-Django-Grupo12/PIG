from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactoForm

# Create your views here.
def inicio(request):
    return render(request, "index.html")

def producto(request, id):
    return render(request, "producto.html", {"id": id, "nombre": "primer producto"})

def about(request):
    return HttpResponse("Acerca de")

def contacto(request):
    #return HttpResponse("Pagina De Contacto")
    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        #Si el método es POST quiere decir que el formulario ya se encuentra lleno
        #Que será enviado al servidor
    else:
        #Si el método "NO" es POST quiere decir que el formulario se encuentra vacío
        #Se renderiza un formulario nuevo vacío
        contacto_form = ContactoForm()
        #se crea una nueva instancia de ContactoForm y se lo asigna a la variabale contacto_form
    return render(request, "contacto.html", {'contacto_form': contacto_form})
