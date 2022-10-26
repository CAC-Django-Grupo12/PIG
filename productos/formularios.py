from django import forms

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
    marca= forms.CharField(max_length=20)       # tabla
    modelo= forms.CharField(max_length=30)      # tabla
    categoria= forms.CharField(max_length=20)   # tabla
    descripcion= forms.CharField(label='Descripción', max_length=300, widget=forms.Textarea(attrs={'class':'form-control','rows':4}))
    # puertas = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[2-5]+', 'title':'entre 2 y 5'}))
    puertas = forms.ChoiceField(choices=PUERTAS,initial='',widget=forms.Select(attrs={'class':'form-control'}))    
    precio= forms.FloatField(label='Precio $')
    # imagen= 


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre:")
    apellido = forms.CharField(label="Apellido:")
    correo = forms.EmailField(label="Correo:")
    mensaje = forms.CharField(label="Mensaje:")
