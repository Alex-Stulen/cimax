from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created_at', 'updated_at')
    list_display_links = ('pk', 'name')
    search_fields = ('pk', 'name')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.FilmConfig)
class FilmConfigAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'is_published', 'film')
    list_display_links = ('pk', 'name')
    search_fields = ('pk', 'name')
    readonly_fields = ('created_at', 'updated_at')

    @staticmethod
    def film(config: models.FilmConfig):
        if hasattr(config, 'film'):
            return config.film.name
        else:
            return '-'


@admin.register(models.Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'original_name', 'film_year', 'film_view_count', 'created_at', 'updated_at')
    list_display_links = ('pk', 'name', 'original_name')
    list_filter = ('categories', 'film_year', 'config__is_published')
    search_fields = ('pk', 'name', 'original_name', 'film_year')
    readonly_fields = ('created_at', 'updated_at')

    @staticmethod
    def film_view_count(film: models.Film):
        return film.film_retrieve_view_set.count()


@admin.register(models.FilmImage)
class FilmImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'film__name')
    list_display_links = ('pk', 'film__name')
    search_fields = ('pk', 'film__name')
    readonly_fields = ('created_at', 'updated_at')

    @staticmethod
    def film__name(film_image: models.FilmImage):
        return film_image.film.name


@admin.register(models.FilmRetrieveView)
class FilmRetrieveViewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'film', 'ip_address', 'ip_info', 'created_at', 'updated_at')
    list_display_links = ('pk', 'film', 'ip_address')
    search_fields = ('pk', 'film__name', 'film__original_name', 'ip_address')
    readonly_fields = ('created_at', 'updated_at')
