from django import forms
from django.forms import ValidationError
from .models import Categoria, Vehiculo

class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields= ['marca', 'modelo', 'anio', 'categoria', 'descripcion', 'puertas', 'precio', 'fecha_publicacion', 'seleccionado', 'imagen', ] 
        #'__all__'
        #exclude= ('campo',)
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'anio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admitimos vehículos de hasta 5 años de antigüedad'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows': 5,'class':'form-control'}),
            'puertas': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control','type':'int'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'imagen': forms.FileInput(attrs={'class':'form-control', 'multiple':True})

        }
        error_messages= {
            'marca': {
                'required': 'No puede estar vacío'
            }            
        }


    # PUERTAS = (
    #     ('','-Seleccione-'),
    #     (2,'2 puertas'),
    #     (3,'2 puertas+portón'),
    #     (4,'3 puertas+portón'),
    #     (5,'4 puertas'),
    #     (6,'4 puertas+portón'),
    # )

    # # id=                                       # autom
    # marca= forms.CharField(max_length=20, error_messages={'required': 'Por favor completa el campo',})       # tabla
    # modelo= forms.CharField(max_length=30)      # tabla
    # anio = forms.IntegerField(initial=2022 , label='Año', min_value=2017, max_value=2022, help_text='admitimos vehículos de hasta 5 años de antigüedad') 
    # categoria= forms.CharField(max_length=20)   # tabla
    # descripcion= forms.CharField(label='Descripción', max_length=300, widget=forms.Textarea(attrs={'class':'form-control','rows':4}))
    # puertas = forms.ChoiceField(choices=PUERTAS,initial='',widget=forms.Select(attrs={'class':'form-control'}))    
    # precio= forms.FloatField(label='Precio $')
    # fecha_publicacion= forms.DateField(label='Fecha publicación')
    # # imagen= 


class CategoriaForm(forms.ModelForm):
    #categoria= forms.CharField(label='Categoría', max_length=20, error_messages={'required': 'Por favor completa el campo',})
    class Meta:
        model = Categoria
        fields= ['categoria']   # opcion: '__all__'
        #exclude= ('campo',)
        widgets = {
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa un nombre'})
        }
        error_messages= {
            'categoria': {
                'required': 'No puede estar vacío'
            }
        }



class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre:")
    apellido = forms.CharField(label="Apellido:")
    correo = forms.EmailField(label="Correo:")
    mensaje = forms.CharField(label="Mensaje:")


class BusquedaForm(forms.Form):

    PUERTAS = (
        ('','-Seleccione-'),
        (2,'2 puertas'),
        (3,'2 puertas+portón'),
        (4,'3 puertas+portón'),
        (5,'4 puertas'),
        (6,'4 puertas+portón'),
    )
 
    marca= forms.CharField(max_length=20, required=False)       # tabla
    modelo= forms.CharField(max_length=30, required=False)      # tabla
    anio = forms.IntegerField( initial=2022 , label='Año', min_value=2017, max_value=2022, help_text='') 
    categoria= forms.CharField(max_length=20, required=False)   # tabla
    puertas = forms.ChoiceField( required=False,choices=PUERTAS,initial='',widget=forms.Select(attrs={'class':'form-control'}))