from django import forms
from django.forms import ValidationError

class Vehiculos(forms.Form):

    PUERTAS = (
        ('','-Seleccione-'),
        (2,'2 puertas'),
        (3,'2 puertas+portón'),
        (4,'3 puertas+portón'),
        (5,'4 puertas'),
        (6,'4 puertas+portón'),
    )


    # id=                                       # autom
    marca= forms.CharField(max_length=20, error_messages={'required': 'Por favor completa el campo',})       # tabla
    modelo= forms.CharField(max_length=30)      # tabla
    anio = forms.IntegerField(initial=2022 , label='Año', min_value=2017, max_value=2022, help_text='admitimos vehículos de hasta 5 años de antigüedad') 
    categoria= forms.CharField(max_length=20)   # tabla
    descripcion= forms.CharField(label='Descripción', max_length=300, widget=forms.Textarea(attrs={'class':'form-control','rows':4}))
    puertas = forms.ChoiceField(choices=PUERTAS,initial='',widget=forms.Select(attrs={'class':'form-control'}))    
    precio= forms.FloatField(label='Precio $')
    # imagen= 


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre:")
    apellido = forms.CharField(label="Apellido:")
    correo = forms.EmailField(label="Correo:")
    mensaje = forms.CharField(label="Mensaje:")