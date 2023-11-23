# Generated by Django 4.2.7 on 2023-11-17 08:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('Codigo', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Fecha', models.DateField()),
                ('Autor', models.CharField(max_length=50)),
                ('Cantidad', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]