from django import forms

class Vehiculos(forms.Form):
    # id=                                       # autom
    marca= forms.CharField(max_length=20)       # tabla
    modelo= forms.CharField(max_length=30)      # tabla
    categoria= forms.CharField(max_length=20)   # tabla
    descripcion= forms.CharField(label='Descripción', widget=forms.Textarea)
    puertas = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[2-5]+', 'title':'entre 2 y 5'}))
    precio= forms.FloatField()
    # imagen= 


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre:")
    apellido = forms.CharField(label="Apellido:")
    correo = forms.EmailField(label="Correo:")
    mensaje = forms.CharField(label="Mensaje:")
