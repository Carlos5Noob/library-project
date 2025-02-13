
from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:book_id>/", views.detail, name='detail'),
    path("autores/", views.author, name='author'),
    path("autores/<int:author_id>/", views.author_detail, name='author_detail'),
    path("generos/", views.genre, name='genero'),
    path("generos/<str:genre_name>/", views.genre_detail, name='genre_detail'),
    path("add-author/", views.form, name='form'),
    path("add-book/", views.form2, name='form2'),
    path("recientes/", views.recientes, name='recientes'),
    path("jonatan/", views.jonatan, name='jonatan'),
]
