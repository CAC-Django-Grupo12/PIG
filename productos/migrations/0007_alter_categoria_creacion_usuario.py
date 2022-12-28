# Generated by Django 3.2 on 2022-12-28 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0006_categoria_creacion_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='creacion_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
