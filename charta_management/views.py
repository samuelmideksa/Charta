from django.shortcuts import render, redirect
from charta_management import models
from charta_management import forms
from charta_management.models import Author


def manage(request):
    count = {}
    count['authors'] = models.Author.objects.count()
    count['genres'] = models.Genre.objects.count()
    count['series'] = models.Series.objects.count()
    count['books'] = models.Book.objects.count()

    return render(request, 'manage.html', {'count': count})


def manage_authors(request):
    authors = models.Author.objects.all()
    if request.method == 'POST':
        if 'delete' in request.POST:
            pk = request.POST.get('delete')
            author = models.Author.objects.get(id=pk)
            author.delete()
            return redirect('manage_authors')
    return render(request, 'authors.html', {'authors': authors})


def manage_genres(request):
    genres = models.Genre.objects.all()
    if request.method == 'POST':
        if 'delete' in request.POST:
            pk = request.POST.get('delete')
            genre = models.Genre.objects.get(id=pk)
            genre.delete()
            return redirect('manage_genres')
    return render(request, 'genres.html', {'genres': genres})


def manage_series(request):
    series = models.Series.objects.all()
    if request.method == 'POST':
        if 'delete' in request.POST:
            pk = request.POST.get('delete')
            series = models.Series.objects.get(id=pk)
            series.delete()
            return redirect('manage_series')
    return render(request, 'series.html', {'series': series})


def manage_books(request):
    books = models.Book.objects.all()
    if request.method == 'POST':
        if 'delete' in request.POST:
            pk = request.POST.get('delete')
            book = models.Book.objects.get(id=pk)
            book.delete()
            return redirect('manage_authors')
    return render(request, 'books.html', {'books': books})


def add_author(request):
    if request.method == 'POST':
        if 'save' in request.POST:
            form = forms.AuthorForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('manage_authors')
        elif 'save-and-add-another' in request.POST:
            form = forms.AuthorForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('add_author')
    else:
        form = forms.AuthorForm()
        return render(request, 'add_author.html', {'form': form})


def add_genre(request):
    if request.method == 'POST':
        if 'save' in request.POST:
            form = forms.GenreForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('manage_genres')
        elif 'save-and-add-another' in request.POST:
            form = forms.GenreForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('add_genre')
    else:
        form = forms.GenreForm()
        return render(request, 'add_genre.html', {'form': form})


def add_series(request):
    if request.method == 'POST':
        if 'save' in request.POST:
            form = forms.SeriesForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('manage_series')
        elif 'save-and-add-another' in request.POST:
            form = forms.SeriesForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('add_series')
    else:
        form = forms.SeriesForm()
        return render(request, 'add_series.html', {'form': form})


def add_book(request):
    if request.method == 'POST':
        if 'save' in request.POST:
            form = forms.BookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('manage_books')
        elif 'save-and-add-another' in request.POST:
            form = forms.BookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('add_book')
    else:
        form = forms.BookForm()
    return render(request, 'add_book.html', {'form': form})


def edit_author(request, author_id):
    author = models.Author.objects.get(pk=author_id)
    if request.method == 'POST':
        if 'save' in request.POST:
            form = forms.AuthorForm(request.POST, request.FILES, instance=author)
            if form.is_valid():
                form.save()
        elif 'delete' in request.POST:
            author.delete()
        return redirect('manage_authors')
    else:
        form = forms.AuthorForm(instance=author)
    return render(request, 'edit_author.html', {'form': form})


def edit_genre(request, genre_id):
    genre = models.Genre.objects.get(pk=genre_id)
    if request.method == 'POST':
        if 'save' in request.POST:
            form = forms.GenreForm(request.POST, request.FILES, instance=genre)
            if form.is_valid():
                form.save()
            return redirect('manage_genres')
        elif 'delete' in request.POST:
            genre.delete()
            return redirect('manage_genres')
    else:
        form = forms.GenreForm(instance=genre)
    return render(request, 'edit_genre.html', {'form': form})


def edit_series(request, series_id):
    series = models.Series.objects.get(pk=series_id)
    if request.method == 'POST':
        if 'save' in request.POST:
            form = forms.SeriesForm(request.POST, request.FILES, instance=series)
            if form.is_valid():
                form.save()
        elif 'delete' in request.POST:
            series.delete()
        return redirect('manage_series')
    else:
        form = forms.SeriesForm(instance=series)
    return render(request, 'edit_series.html', {'form': form})


def edit_book(request, book_id):
    book = models.Book.objects.get(pk=book_id)
    if request.method == 'POST':
        if 'save' in request.POST:
            form = forms.BookForm(request.POST, request.FILES, instance=book)
            if form.is_valid():
                form.save()
        elif 'delete' in request.POST:
            book.delete()
        return redirect('manage_books')
    else:
        form = forms.BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})
