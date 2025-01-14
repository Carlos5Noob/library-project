from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', context={'books': books})
