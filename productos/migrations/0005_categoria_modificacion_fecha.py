# Generated by Django 3.2 on 2022-12-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_categoria_creacion_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='modificacion_fecha',
            field=models.DateTimeField(null=True),
        ),
    ]
