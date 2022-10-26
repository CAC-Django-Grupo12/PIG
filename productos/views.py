from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .formularios import Vehiculos,ContactoForm


def inicio(request):
    # return render(request, "index.html")
    return redirect('index')

def index(request):
    listado_vehiculos = [
        {
            'marca': 'TOYOTA',
            'modelo': 'Yaris',
            'categoria': 'Sedán',
            'descripcion': 'Año 2021, color azul, caja automática, 10.000 Km ',
            'puertas': '4',
            'precio': 4000000
        },
        {
            'marca': 'FIAT',
            'modelo': 'Palio',
            'categoria': 'Hachback',
            'descripcion': 'Año 2016, color blanco, 70.000 Km ',
            'puertas': '5',
            'precio': 2000000
        },
        {
            'marca': 'TOYOTA',
            'modelo': 'Corolla',
            'categoria': 'Sedán',
            'descripcion': 'Año 2020, Cololr gris, caja automática, 20.000 Km ',
            'puertas': '4',
            'precio': 4800000
        },
        ]

    return render(request, 'index.html',
                  {'listado_vehiculos': listado_vehiculos})


def vehiculo(request):
    if request.method == 'POST':
        # print(request.POST)
        form = Vehiculos(request.POST)
        if form.is_valid():
            # guardar 
            messages.success(request,'Vehículo agregado OK')
            #return HttpResponse("vehiculo OK :)")         #HttpResponseRedirect('')
        else:
            messages.warning(request,'Por favor revisa los errores')
    else:
        # print(request.GET)
        form = Vehiculos()
   
    return render(request, 'vehiculo.html', {'form': form})

def about(request):
    return HttpResponse("Acerca de")

def resultado(request):
    listado_vehiculos = [
        {
            'marca': 'TOYOTA',
            'modelo': 'Yaris',
            'categoria': 'Sedán',
            'descripcion': 'Año 2021, color azul, caja automática, 10.000 Km ',
            'puertas': '4',
            'precio': 4000000
        },
        {
            'marca': 'FIAT',
            'modelo': 'Palio',
            'categoria': 'Hachback',
            'descripcion': 'Año 2016, color blanco, 70.000 Km ',
            'puertas': '5',
            'precio': 2000000
        },
        {
            'marca': 'TOYOTA',
            'modelo': 'Corolla',
            'categoria': 'Sedán',
            'descripcion': 'Año 2020, Cololr gris, caja automática, 20.000 Km ',
            'puertas': '4',
            'precio': 4800000
        },
        {
            'marca': 'FORD',
            'modelo': 'Focus',
            'categoria': 'Sedán',
            'descripcion': 'Año 2000, Cololr gris, caja automática, 20.000 Km ',
            'puertas': '4',
            'precio': 4800000
        },
        ]

    return render(request, 'resultados.html',
                  {'listado_vehiculos': listado_vehiculos})


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

def producto(request, id):
    return render(request, "producto.html", {"id": id, "nombre": "primer producto"})

def nada(request):
    return render(request, "nada.html")

