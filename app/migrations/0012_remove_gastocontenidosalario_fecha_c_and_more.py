# Generated by Django 4.2.7 on 2024-01-13 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_gastocontenidosalario_ingresogenera_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gastocontenidosalario',
            name='Fecha_c',
        ),
        migrations.RemoveField(
            model_name='gastocontenidosalario',
            name='Titulo',
        ),
        migrations.AddField(
            model_name='gastocontenidosalario',
            name='contenido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.contenido'),
        ),
        migrations.AlterField(
            model_name='gastocontenidosalario',
            name='DNIT',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.trabajador'),
        ),
        migrations.AlterModelTable(
            name='gastocontenidosalario',
            table=None,
        ),
    ]
