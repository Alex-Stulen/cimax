import os

from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Category'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.name


class FilmConfig(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Film config name'
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name='Is published film'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.name


class FilmManager(models.Manager):
    def all(self):
        return self.filter(config__is_published=True)


class Film(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Film name'
    )
    original_name = models.CharField(
        max_length=255,
        verbose_name='Original film name'
    )
    film = models.FileField(
        upload_to='simple_film/films/%Y/%m/%d/'
    )
    film_trailer = models.FileField(
        upload_to='simple_film/films_trailer/%Y/%m/%d/'
    )
    film_year = models.PositiveIntegerField(
        verbose_name='Film production year'
    )
    poster = models.ImageField(
        upload_to='simple_film/posters/%Y/%m/%d/',
        verbose_name='Film poster'
    )
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    config = models.OneToOneField(
        FilmConfig,
        on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = FilmManager()

    class Meta:
        ordering = ('-created_at', )

    def delete(self, using=None, keep_parents=False):
        if os.path.exists(self.film.path):
            try:
                os.remove(self.film.path)
            except:
                pass
        
        if os.path.exists(self.film_trailer.path):
            try:
                os.remove(self.film_trailer.path)
            except:
                pass
        
        if os.path.exists(self.poster.path):
            try:
                os.remove(self.poster.path)
            except:
                pass
        
        return super().delete(using=None, keep_parents=False)

    def __str__(self):
        return self.name
