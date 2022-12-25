from productos.models import Vehiculo, Categoria
import pandas as pd



def run():
   

    # carga el archivo en un data frame  
    df = pd.read_excel('Automoviles-AFIP-2021.xlsx', sheet_name='autos')

    for i in range(10):          #len(df)):
        print(i)
        cat= df.iloc[i]['categoria']
        categoria=Categoria.objects.get(id=cat)
        vehiculo=Vehiculo(
                marca= df.iloc[i]['marca'],
                modelo= df.iloc[i]['modelo'],
                anio = df.iloc[i]['anio'],
                categoria= categoria,
                puertas = 4,
                descripcion=df.iloc[i]['tipo'],
                precio=df.iloc[i]['valor'],
                fecha_publicacion= "2022-12-01",
                imagen= 'upload/yaris1.jpg',
                seleccionado=df.iloc[i]['seleccionado'])
    
        vehiculo.save()