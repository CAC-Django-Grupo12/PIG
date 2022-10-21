from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .formularios import Vehiculos


def inicio(request):
    return render(request, "index.html")

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
        print(request.POST)
        form = Vehiculos(request.POST)
        if form.is_valid():
            return HttpResponse("vehiculo OK :)")         #HttpResponseRedirect('')
    else:
        print(request.GET)
        form = Vehiculos()
   
    return render(request, 'vehiculo.html', {'form': form})

def about(request):
    return HttpResponse("Acerca de")