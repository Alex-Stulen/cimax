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

    def __str__(self):
        return self.name


class FilmImage(models.Model):
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name='film_images_set'
    )

    image = models.ImageField(
        upload_to='simple_film/images/%Y/%m/%d/',
        verbose_name='Film Image'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.film.name


class FilmRetrieveView(models.Model):
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name='film_retrieve_view_set'
    )

    ip_address = models.GenericIPAddressField()
    ip_info = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )
