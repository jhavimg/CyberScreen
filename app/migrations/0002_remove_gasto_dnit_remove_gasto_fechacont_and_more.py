# Generated by Django 4.2.7 on 2023-12-28 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasto',
            name='DNIT',
        ),
        migrations.RemoveField(
            model_name='gasto',
            name='FechaCont',
        ),
        migrations.RemoveField(
            model_name='gasto',
            name='Titulo',
        ),
    ]
