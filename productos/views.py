from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from productos.models import Vehiculo, Categoria, Contacto

from .formularios import VehiculoForm,ContactoForm, BusquedaForm, CategoriaForm

from django.views.generic import ListView
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#Import para enviar correos
from django.conf import settings
from django.core.mail import send_mail

from django.core.paginator import Paginator


def inicio(request):
    # return render(request, "index.html")
    return redirect('index')

def index(request):

    listado_vehiculos=Vehiculo.objects.all().select_related('categoria')
    listado_vehiculos=Vehiculo.objects.filter(seleccionado=True).select_related('categoria')
 
    return render(request, 'inicial.html',
                  {'listado_vehiculos': listado_vehiculos})


class VehiculosListView(LoginRequiredMixin, ListView):
    paginate_by= 5
    model = Vehiculo
    context_object_name= 'vehiculos'
    template_name= 'vehiculos_index.html'

class VehiculoView(LoginRequiredMixin, View):
    form_class = VehiculoForm
    #initial = {'key': 'value'}
    template_name = 'vehiculo_nuevo.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()    #initial= self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()

            except:
                form.add_error('vehiculo', str(ve))
            else:
                return redirect('vehiculos_index')
        
        return render(request, self.template_name, {'form': form})

@login_required
def vehiculo_eliminar(request,id):
    vehiculo = Vehiculo.objects.get(pk=id)
    vehiculo.delete()
    return redirect('vehiculos_index')

@login_required
def vehiculo_editar(request,id):
    vehiculo = Vehiculo.objects.get(pk=id)
    if(request.method=='POST'):
        form = VehiculoForm(request.POST, request.FILES, instance=vehiculo)
        if form.is_valid():
            vehiculo.save()
            return redirect('vehiculos_index')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request,'vehiculo_editar.html',{'form':form, 'id': id})


# def vehiculo(request):
#     if request.method == 'POST':
#         # print(request.POST)
#         form = VehiculoForm(request.POST)
#         if form.is_valid():
#             # guardar 
#             marca = form.cleaned_data['marca']
#             modelo = form.cleaned_data['modelo']
#             anio = form.cleaned_data['anio']
#             #categoria = form.cleaned_data['categoria']
#             descripcion = form.cleaned_data['descripcion']
#             puertas = form.cleaned_data['puertas']
#             precio = form.cleaned_data['precio']
#             fecha_publicacion = form.cleaned_data['fecha_publicacion']
#             nuevo_vehiculo = Vehiculo(
#                 marca=marca, 
#                 modelo=modelo, 
#                 anio=anio, 
#                 #categoria=categoria, 
#                 descripcion=descripcion, 
#                 puertas=puertas,
#                 precio=precio, 
#                 fecha_publicacion=fecha_publicacion)
#             nuevo_vehiculo.save()

#             messages.success(request,'Vehículo agregado OK')
#             #return HttpResponse("vehiculo OK :)")         #HttpResponseRedirect('')
#         else:
#             messages.warning(request,'Por favor revisa los errores')
#     else:
#         # print(request.GET)
#         form = VehiculoForm()
   
#     return render(request, 'vehiculo.html', {'form': form})



# ------------------------------------------------
# Categorias
# def categorias_index(request):
#     categorias = Categoria.objects.all()
#     return render(request, 'categorias_index.html',{'categorias': categorias})
class CategoriasListView(LoginRequiredMixin, ListView):
    model = Categoria
    context_object_name= 'categorias'
    template_name= 'categorias_index.html'
    #ordering= ['id']


# def categoria_nueva(request):
#     if request.method == 'POST':
#         form = CategoriaForm(request.POST)
#         if form.is_valid():
#             categoria = form.cleaned_data['categoria']
#             nueva_categoria = Categoria(categoria=categoria)
#             nueva_categoria.save()
#             #messages.success(request,'Categoría agregada OK')
#             return redirect('categorias_index')
#         else:
#             messages.warning(request,'Por favor revisa los errores')
#     else:
#         form = CategoriaForm()
   
#     return render(request, 'categoria_nueva.html', {'form': form})

class CategoriaView(LoginRequiredMixin, View):
    form_class = CategoriaForm
    #initial = {'key': 'value'}
    template_name = 'categoria_nueva.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()    #initial= self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error('categoria', str(ve))
            else:
                return redirect('categorias_index')
        
        return render(request, self.template_name, {'form': form})



@login_required
def categoria_eliminar(request,id):
    categoria = Categoria.objects.get(pk=id)
    categoria.delete()
    return redirect('categorias_index')

@login_required
def categoria_editar(request,id):
    categoria = Categoria.objects.get(pk=id)
    if(request.method=='POST'):
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria.save()
            return redirect('categorias_index')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request,'categoria_editar.html',{'form':form, 'id': id})



def about(request):
    return HttpResponse("Acerca de")


def resultado(request):

    listado_vehiculos=Vehiculo.objects.all().select_related('categoria')

    return render(request, 'resultados.html',
                  {'listado_vehiculos': listado_vehiculos})



def contacto(request):
    #return HttpResponse("Pagina De Contacto")
    if request.method == "POST":
        contacto_form = ContactoForm(request.POST)
        #Si el método es POST quiere decir que el formulario ya se encuentra lleno
        #Que será enviado al servidor
        contacto_form.is_valid()
        nombre = contacto_form.cleaned_data['nombre']
        apellido = contacto_form.cleaned_data['apellido']
        correo = contacto_form.cleaned_data['correo']
        mensaje = contacto_form.cleaned_data['mensaje']
        nuevo_contacto = Contacto(nombre=nombre, apellido=apellido, correo=correo, mensaje=mensaje)
        nuevo_contacto.save()
        
        subject = nuevo_contacto.nombre + " " + nuevo_contacto.apellido
        from_email = nuevo_contacto.correo
        message = nuevo_contacto.correo + " " + nuevo_contacto.mensaje
        recipient_list = [settings.EMAIL_HOST_USER]
        
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False
            )

        return redirect('inicio')
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

        if (form.is_valid()):
            
            listado_vehiculos=Vehiculo.objects.all()
            
            if form.cleaned_data['marca']:
                listado_vehiculos=Vehiculo.objects.filter(marca__icontains=form.cleaned_data['marca']).select_related('categoria')
            if form.cleaned_data['modelo']:
                 listado_vehiculos=listado_vehiculos.filter(modelo__icontains=form.cleaned_data['modelo']).select_related('categoria')
            if form.cleaned_data['aniodesde']:
                 listado_vehiculos=listado_vehiculos.filter(anio__gte=form.cleaned_data['aniodesde']).select_related('categoria')
            if form.cleaned_data['aniohasta']:
                 listado_vehiculos=listado_vehiculos.filter(anio__lte=form.cleaned_data['aniohasta']).select_related('categoria')
            
            return render(request, 'resultados_busqueda.html',
                        {'listado_vehiculos': listado_vehiculos})

        else:
            messages.warning(request,'Por favor revisa los errores')
    else:
         
        form = BusquedaForm()
   
    return render(request, 'buscar.html', {'form': form})

