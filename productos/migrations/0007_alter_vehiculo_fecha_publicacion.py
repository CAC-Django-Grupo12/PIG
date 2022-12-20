# Generated by Django 3.2 on 2022-12-15 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_alter_vehiculo_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='fecha_publicacion',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha publicación'),
        ),
    ]
