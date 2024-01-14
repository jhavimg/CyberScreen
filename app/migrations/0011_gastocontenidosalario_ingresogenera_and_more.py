# Generated by Django 4.2.7 on 2024-01-13 18:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_incluye_datos_suscripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GastoContenidoSalario',
            fields=[
                ('Codigo', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Fecha', models.DateField()),
                ('Autor', models.CharField(max_length=255)),
                ('Fecha_c', models.DateField()),
                ('Cantidad', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('DNIT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trabajador')),
                ('Titulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.contenido')),
            ],
            options={
                'db_table': 'Gasto-Contenido-Salario',
            },
        ),
        migrations.CreateModel(
            name='IngresoGenera',
            fields=[
                ('Codigo', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Fecha', models.DateField()),
                ('Autor', models.CharField(max_length=50)),
                ('Cantidad', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('DatosSuscripcion', models.ForeignKey(db_column='DatosSuscripción', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.suscripcion')),
            ],
        ),
        migrations.RemoveField(
            model_name='gastocontenido',
            name='contenido',
        ),
        migrations.RemoveField(
            model_name='gastocontenido',
            name='gasto',
        ),
        migrations.DeleteModel(
            name='Ingreso',
        ),
        migrations.DeleteModel(
            name='Gasto',
        ),
        migrations.DeleteModel(
            name='GastoContenido',
        ),
    ]