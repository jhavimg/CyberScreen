# Generated by Django 4.2.7 on 2024-01-13 16:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_delete_incluye'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incluye',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=100)),
                ('Fecha', models.DateField(default=datetime.date(2024, 1, 1))),
                ('contenido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.contenido')),
                ('datos_suscripcion', models.ForeignKey(db_column='DatosSuscripción', on_delete=django.db.models.deletion.CASCADE, to='app.suscripcion')),
            ],
        ),
    ]