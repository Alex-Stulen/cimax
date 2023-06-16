from django.db.models.signals import post_delete
from django.dispatch import receiver

from . import models


@receiver(post_delete, sender=models.Film)
def delete_film_images_file(sender, instance: models.Film, **kwargs):
    instance.film.delete()
    instance.film_trailer.delete()
    instance.poster.delete()


@receiver(post_delete, sender=models.FilmImage)
def delete_film_image_image_file(sender, instance: models.FilmImage, **kwargs):
    instance.image.delete()
