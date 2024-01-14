from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contenido, Suscripcion, Incluye

@receiver(post_save, sender=Contenido)
def crear_incluye_para_nuevo_contenido(sender, instance, created, **kwargs):
    if created:
        suscripciones = Suscripcion.objects.all()
        for suscripcion in suscripciones:
            Incluye.objects.create(contenido=instance, datos_suscripcion=suscripcion)

@receiver(post_save, sender=Suscripcion)
def crear_incluye_para_nueva_suscripcion(sender, instance, created, **kwargs):
    if created:
        contenidos = Contenido.objects.all()
        for contenido in contenidos:
            Incluye.objects.create(contenido=contenido, datos_suscripcion=instance)
