from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Book, Author, Genre


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', context={'books': books})

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', context={'book': book})

def author(request):
    autores = Author.objects.all()
    return render(request, "books/autores.html", context={"autores": autores})

def author_detail(request, author_id):
    autor = get_object_or_404(Author, pk=author_id)
    libros = Book.objects.filter(authors=autor)
    return render(request, template_name="books/autordetail.html", context={"autor": autor, "libros": libros})

def genre(request):
    generos = Genre.objects.all()
    return render(request, template_name="books/generos.html", context={"generos": generos})

def genre_detail(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)
    libros = Book.objects.filter(genre=genre)
    return render(request, template_name="books/librosgen.html", context={"genre": genre, "libros": libros})