from django.db import models
from .validators import isbn_validator


class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author_images/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    plot = models.TextField(null=True, blank=True)

    def authors_list(self):
        return [author.name for author in self.authors.all()]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True, blank=True)
    series_number = models.PositiveIntegerField(null=True, blank=True)
    cover_image = models.ImageField()
    genres = models.ManyToManyField(Genre)
    isbn = models.CharField(max_length=18, validators=[isbn_validator], null=True, blank=True, unique=True)
    added_date = models.DateField(auto_now_add=True)
    publisher = models.CharField(max_length=200)
    published_date = models.DateField()
    languages = models.CharField(max_length=200, null=True)
    plot = models.TextField(null=True)
    book_file = models.FileField()

    def authors_list(self):
        return [author.name for author in self.authors.all()]

    def genres_list(self):
        return [genre.name for genre in self.genres.all()]

    def languages_list(self):
        return [language.name for language in self.languages.all()]

    def __str__(self):
        return f'{self.title} - {self.authors}'
