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

#Paginacion
from django.core.paginator import Paginator

#Import para generar PDF
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm
import qrcode
from os import remove
import matplotlib.pyplot as plt

import os



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
                messages.success(request,'Vehículo agregado OK')          

            except:
                messages.error(request,'Ocurrió un error al agregar vehículo...')
                #form.add_error('vehiculo', str(ve))
            else:
                return redirect('vehiculos_index')
        
        return render(request, self.template_name, {'form': form})

@login_required
def vehiculo_eliminar(request,id):
    try:
        vehiculo = Vehiculo.objects.get(pk=id)
        
        # comprueba y elimina imagen
        if os.path.exists('.'+vehiculo.imagen.url) and os.path.isfile('.'+vehiculo.imagen.url):
            try:
                os.remove('.'+vehiculo.imagen.url)
                messages.error(request,'Imagen eliminada OK'+' -ID: '+str(id))
            except:
                messages.error(request,'No se encontró la imagen para eliminar...'+' -ID: '+str(id))
        
        vehiculo.delete()
        messages.error(request,'Vehículo eliminado OK') 
    except:
        messages.error(request,'Error al eliminar vehículo...') 

    return redirect('vehiculos_index')

@login_required
def vehiculo_editar(request,id):
    try:
        vehiculo = Vehiculo.objects.get(pk=id)
        if(request.method=='POST'):
            form = VehiculoForm(request.POST, request.FILES, instance=vehiculo)
            if form.is_valid():
                vehiculo.save()
                messages.info(request,'Vehículo modificado OK')
                return redirect('vehiculos_index')
        else:
            form = VehiculoForm(instance=vehiculo)
        return render(request,'vehiculo_editar.html',{'form':form, 'id': id})
    except:
        messages.error(request,'Error al editar vehículo...') 
        return redirect('vehiculos_index')

@login_required
def vehiculo_duplicar(request,id):
    vehiculo_origen = Vehiculo.objects.get(pk=id)

    vehiculo = Vehiculo(
        marca=vehiculo_origen.marca, 
        modelo=vehiculo_origen.modelo, 
        anio=vehiculo_origen.anio, 
        categoria=vehiculo_origen.categoria, 
        puertas=vehiculo_origen.puertas,
        precio=vehiculo_origen.precio,
        imagen=vehiculo_origen.imagen,
    )

    if(request.method=='POST'):
        form = VehiculoForm(request.POST, request.FILES, instance=vehiculo    )
        if form.is_valid():
            vehiculo.save()
            messages.info(request,'Vehículo duplicado OK')
            return redirect('vehiculos_index')
    else:
        form = VehiculoForm(instance= vehiculo)
    return render(request,'vehiculo_duplicar.html',{'form':form, 'id': id})


@login_required
def vehiculo_pdf(request,id):
    try:
        vehiculo = Vehiculo.objects.get(pk=id)
        try:

            # Create a file-like buffer to receive PDF data.
            buffer = io.BytesIO()

            # Create the PDF object, using the buffer as its "file."
            p = canvas.Canvas(buffer)

            # Draw things on the PDF. Here's where the PDF generation happens.
            # See the ReportLab documentation for the full list of functionality.
            
            p.drawString       (100, 800, vehiculo.marca+" "+vehiculo.modelo)
            p.drawString       (100, 780, vehiculo.categoria.categoria)
            
            p.line             (100,760,500,760)     #linea
            
            imagen = ImageReader('.'+vehiculo.imagen.url)
            #imagen= ImageReader('https://picsum.photos/300/200')
            p.drawImage(imagen,  100,600, width=60*mm, height=40*mm , mask=None, preserveAspectRatio=True)

            # QR
            qr = qrcode.make('http://127.0.0.1:8000/accounts/login/')
            qr_file = open(".\static\img\qr.png", "wb")     #mejorar esto
            qr.save(qr_file)
            qr_file.close()
            imagen = ImageReader(".\static\img\qr.png")     #
            p.drawImage(imagen,  350, 400,  width=50*mm , preserveAspectRatio=True)
            remove(".\static\img\qr.png")


            # Grafico
                                    # advierte error por consola, funciona ok
            # datos
            # meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,]
            # ventas = [200, 180, 250, 310, 290, 250, 220, 180, 200, 280, 350, 300]
            # plt.bar(meses, ventas)
            
            fig, ax = plt.subplots()
            marcas = ['Toyota', 'Fiat', 'Ford', 'VolksWagen']
            counts = [100, 60, 30, 55]
            bar_labels = ['Toyota', 'Fiat', 'Ford', 'VW']
            bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

            ax.bar(marcas, counts, label=bar_labels, color=bar_colors)

            ax.set_ylabel('Ventas [unidades]')
            ax.set_xlabel('Principales Marcas')
            ax.set_title('Ventas por marcas')
            ax.legend(title='Colores')

            plt.savefig(".\static\img\grafico.png")             #
            imagen = ImageReader(".\static\img\grafico.png")    #
            p.drawImage(imagen,  100, 100,  width=100*mm , preserveAspectRatio=True)
            remove(".\static\img\grafico.png")                  #



            # Close the PDF object cleanly, and we're done.
            p.showPage()
            p.save()

            # FileResponse sets the Content-Disposition header so that browsers
            # present the option to save the file.
            buffer.seek(0)

            #messages.info(request,'PDF generado OK')   
            return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

            # return redirect('vehiculos_index')
        except:
            messages.info(request,'Error al generar el PDF')   
            return redirect('Error404')

    except:
        messages.info(request,'Error al generar el PDF /')   
        return redirect('Error404')


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
                messages.success(request,'Categoría agregada OK')   
            except:
                form.add_error('categoria', str(ve))
            else:
                return redirect('categorias_index')
        
        return render(request, self.template_name, {'form': form})



@login_required
def categoria_eliminar(request,id):
    try:
        categoria = Categoria.objects.get(pk=id)
        categoria.delete()
        messages.error(request,'Categoría eliminada OK')   
        return redirect('categorias_index')
    except:     # Categoria.DoesNotExist:
        return redirect('Error404')


@login_required
def categoria_editar(request,id):
    try:
        categoria = Categoria.objects.get(pk=id)
        if(request.method=='POST'):
            form = CategoriaForm(request.POST, instance=categoria)
            if form.is_valid():
                try:
                    categoria.save()
                    messages.info(request,'Categoría modificada OK')   
                    return redirect('categorias_index')
                except:     # Categoria.DoesNotExist:
                    return redirect('Error404')

        else:
            form = CategoriaForm(instance=categoria)
        return render(request,'categoria_editar.html',{'form':form, 'id': id})
    except:
        return redirect('Error404')




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


def Error404(request):
    return render(request, "Error404.html")