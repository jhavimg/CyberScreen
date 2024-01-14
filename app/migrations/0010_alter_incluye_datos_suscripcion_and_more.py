# Generated by Django 4.2.7 on 2024-01-13 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_incluye'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incluye',
            name='datos_suscripcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.suscripcion'),
        ),
        migrations.AlterUniqueTogether(
            name='incluye',
            unique_together={('contenido', 'datos_suscripcion')},
        ),
        migrations.AlterModelTable(
            name='incluye',
            table='Incluye',
        ),
        migrations.RemoveField(
            model_name='incluye',
            name='Fecha',
        ),
        migrations.RemoveField(
            model_name='incluye',
            name='Titulo',
        ),
    ]