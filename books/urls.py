
from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:book_id>/", views.detail, name='detail'),
    path("autores/", views.author, name='author'),
]
