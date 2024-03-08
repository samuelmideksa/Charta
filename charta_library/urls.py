from django.urls import path
from charta_library import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('explore', views.explore, name='explore'),
    path('explore/<int:genre_id>/<slug:genre_name>', views.explore_genre, name='explore_genre'),
    path('author/<int:author_id>/<slug:author_name>', views.author_details, name='author_details'),
    path('search/', views.search_results, name='search_results'),
    path('book/<int:book_id>/<slug:book_title>', views.book_details, name='book_details'),
    path('series/<int:series_id>/<slug:series_title>/', views.series_details, name='series_details'),
]
