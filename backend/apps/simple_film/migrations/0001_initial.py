# Generated by Django 4.2.2 on 2023-06-12 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FilmConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Film config name')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published film')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Film name')),
                ('original_name', models.CharField(max_length=255, verbose_name='Original film name')),
                ('film', models.FileField(upload_to='simple_film/films/%Y/%m/%d/')),
                ('film_year', models.PositiveIntegerField(verbose_name='Film production year')),
                ('poster', models.ImageField(upload_to='simple_film/posters/%Y/%m/%d/', verbose_name='Film poster')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='simple_film.category')),
                ('config', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='simple_film.filmconfig')),
            ],
        ),
    ]
