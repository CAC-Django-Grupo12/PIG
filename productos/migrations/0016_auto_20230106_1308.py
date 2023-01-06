# Generated by Django 3.2 on 2023-01-06 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0015_alter_categoria_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='categoria',
            field=models.ForeignKey(limit_choices_to={'eliminacion_fecha__isnull': True}, on_delete=django.db.models.deletion.PROTECT, to='productos.categoria', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='imagen',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='upload/', verbose_name='Imagen:'),
        ),
    ]