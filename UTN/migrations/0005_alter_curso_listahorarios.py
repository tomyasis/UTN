# Generated by Django 4.2.4 on 2023-11-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTN', '0004_profesor_apellido_profesor_correo_profesor_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='listaHorarios',
            field=models.CharField(max_length=255),
        ),
    ]