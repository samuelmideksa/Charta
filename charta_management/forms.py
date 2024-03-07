from django import forms
from charta_management import models


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author

        fields = ['name', 'image', 'bio']


class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre

        fields = ['name', 'description']


class SeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series

        fields = ['name', 'authors', 'plot']


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book

        fields = ['title', 'authors', 'series', 'series_number', 'cover_image', 'genres', 'isbn', 'publisher', 'published_date', 'languages', 'plot', 'book_file']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'})
        }