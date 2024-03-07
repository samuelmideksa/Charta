from django.urls import path
from charta_library import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('explore', views.explore, name='explore'),
    path('explore/<str:genre_name>', views.explore_genre, name='explore_genre'),
    path('author/<int:author_id>/<str:author_name>', views.author_details, name='author_details'),
    path('search/', views.search_results, name='search_results'),
    path('book/<int:book_id>/<str:book_title>', views.book_details, name='book_details')
]
