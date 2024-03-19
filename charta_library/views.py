from django.shortcuts import render, redirect, get_object_or_404
from charta_management import models
import datetime
import random
from django.db.models import Q
from users import models as user_models
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return redirect('home')


def home(request):
    all_genres = models.Genre.objects.all()

    # Select three random genres
    random_genres = random.sample(list(all_genres), 3)

    book_lists = {}

    # Retrieve 12 books for each randomly selected genre
    for genre in random_genres:
        books = models.Book.objects.filter(genres=genre)[:12]
        book_lists[genre] = books

    context = {'book_lists': book_lists}
    return render(request, 'home.html', context)


def book_details(request, book_id, book_title):
    book = get_object_or_404(models.Book, pk=book_id)
    series_id = book.series.id if book.series else None

    context = {'book': book, 'series_id': series_id}

    if request.method == 'POST':
        rating = request.POST.get('rating')
        review = request.POST.get('reviewText')

        # Check if the user is logged in
        if request.user.is_authenticated:
            try:
                user_book_review = user_models.UserReview.objects.get(user=request.user, book=book)
            except ObjectDoesNotExist:
                user_book_review = None

            # Check if the user has not reviewed the book yet
            if user_book_review is None:
                user = request.user
                # Create a new UserReview object
                user_models.UserReview.objects.create(book=book, rating=rating, review=review, user=user)
                # Redirect to the same page to avoid form resubmission on page refresh
                return redirect('book_details', book_id=book_id, book_title=book_title)

    return render(request, 'book_details.html', context)


def series_details(request, series_id, series_title):
    series = models.Series.objects.get(pk=series_id)
    series_books = models.Book.objects.filter(series=series).order_by('series_number')

    return render(request, 'series_details.html', {'series': series, 'series_books': series_books})


def author_details(request, author_id, author_name):
    author = models.Author.objects.get(pk=author_id)

    all_books = models.Book.objects.filter(authors=author)
    one_year_ago = datetime.datetime.now() - datetime.timedelta(days=365)
    latest_books = all_books.filter(published_date__lte=one_year_ago).order_by('published_date')

    context = {'author': author, 'all_books': all_books, 'latest_books': latest_books}

    return render(request, 'author_details.html', context)


def explore(request):
    genres = models.Genre.objects.order_by('name')
    return render(request, 'explore.html', {'genres': genres})


def explore_genre(request, genre_id, genre_name):
    genre = models.Genre.objects.get(pk=genre_id)

    all_books = models.Book.objects.filter(genres=genre)
    one_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
    recently_added_books = all_books.filter(added_date__lte=one_week_ago)

    # Get all unique author ids from the books
    author_ids = set()
    for book in all_books:
        author_ids.update(book.authors.all().values_list('id', flat=True))

    context = {
        'genre': genre,
        'all_books': all_books,
        'recently_added_books': recently_added_books,
        'author_ids': author_ids,  # Pass the author ids to the template
    }

    return render(request, 'explore_genre.html', context)


def search_results(request):
    query = request.GET.get('q')
    if query:
        results = models.Book.objects.filter(
            Q(title__icontains=query) |
            Q(authors__name__icontains=query) |
            Q(genres__name__icontains=query) |
            Q(series__name__icontains=query) |
            Q(isbn=query)
        ).distinct()
    else:
        results = None

    # Get all unique author ids from the books
    author_ids = set()
    for book in results:
        author_ids.update(book.authors.all().values_list('id', flat=True))

    context = {
        'query': query,
        'results': results,
        'author_ids': author_ids,
    }

    return render(request, 'search_results.html', context)
