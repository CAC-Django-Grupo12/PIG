# Generated by Django 3.2 on 2023-01-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0014_alter_categoria_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria',
            field=models.CharField(max_length=20, verbose_name='Categoría'),
        ),
    ]
