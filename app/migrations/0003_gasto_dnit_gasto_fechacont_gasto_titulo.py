# Generated by Django 4.2.7 on 2023-12-28 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_gasto_dnit_remove_gasto_fechacont_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasto',
            name='DNIT',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='gasto',
            name='FechaCont',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='gasto',
            name='Titulo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
