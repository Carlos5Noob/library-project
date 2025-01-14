from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Book, Author


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