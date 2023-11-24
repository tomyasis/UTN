# Generated by Django 4.2.4 on 2023-11-22 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UTN', '0005_alter_curso_listahorarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='Inscripcion',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='UTN.inscripcion'),
        ),
        migrations.AddField(
            model_name='notaevaluacion',
            name='Inscripcion',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='UTN.inscripcion'),
        ),
    ]