# Generated by Django 3.2 on 2022-12-28 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_alter_vehiculo_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='creacion_fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
