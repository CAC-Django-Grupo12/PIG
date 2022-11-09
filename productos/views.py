from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from productos.models import Vehiculo

from .formularios import VehiculoForm,ContactoForm, BusquedaForm, CategoriaForm


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
        form = VehiculoForm(request.POST)
        if form.is_valid():
            # guardar 
            messages.success(request,'Vehículo agregado OK')
            #return HttpResponse("vehiculo OK :)")         #HttpResponseRedirect('')
        else:
            messages.warning(request,'Por favor revisa los errores')
    else:
        # print(request.GET)
        form = VehiculoForm()
   
    return render(request, 'vehiculo.html', {'form': form})


def categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            # guarda
            messages.success(request,'Categoría agregada OK')
        else:
            messages.warning(request,'Por favor revisa los errores')
    else:
        form = CategoriaForm()
   
    return render(request, 'categoria.html', {'form': form})


def about(request):
    return HttpResponse("Acerca de")


def resultado(request):

    listado_vehiculos=Vehiculo.objects.all().select_related('categoria')

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
    informacion=Vehiculo.objects.select_related('categoria').get(id=id)
    # informacion=Vehiculo.objects.get(id=id).select_related('categoria')
    return render(request, "producto.html", {"informacion": informacion, "nombre": "primer producto"})

def nada(request):
    return render(request, "nada.html")


def buscar(request):
    if request.method == 'POST':
         
        form = BusquedaForm(request.POST)

        if form.is_valid():
            # messages.success(request,'Vehículo agregado OK')
             
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

            return render(request, 'resultados_busqueda.html',
                  {'listado_vehiculos': listado_vehiculos})

        else:
            messages.warning(request,'Por favor revisa los errores')
    else:
         
        form = BusquedaForm()
   
    return render(request, 'buscar.html', {'form': form})

