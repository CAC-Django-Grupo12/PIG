# Generated by Django 3.2 on 2022-12-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_vehiculo_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='precio',
            field=models.DecimalField(decimal_places=0, max_digits=12),
        ),
    ]