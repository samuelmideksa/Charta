from django.urls import path
from charta_management import views

urlpatterns = [
                  path('manage', views.manage, name='manage'),
                  path('manage/authors', views.manage_authors, name='manage_authors'),
                  path('manage/genres', views.manage_genres, name='manage_genres'),
                  path('manage/series', views.manage_series, name='manage_series'),
                  path('manage/books', views.manage_books, name='manage_books'),
                  path('manage/authors/add-author', views.add_author, name='add_author'),
                  path('manage/genres/add-genres', views.add_genre, name='add_genre'),
                  path('manage/series/add-series', views.add_series, name='add_series'),
                  path('manage/books/add-books', views.add_book, name='add_book'),
                  path('manage/authors/edit-author/<int:author_id>', views.edit_author, name='edit_author'),
                  path('manage/genre/edit-genre/<int:genre_id>', views.edit_genre, name='edit_genre'),
                  path('manage/series/edit-series/<int:series_id>', views.edit_series, name='edit_series'),
                  path('manage/books/edit-book/<int:book_id>', views.edit_book, name='edit_book'),
              ]
