from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.shortcuts import get_object_or_404



from .models import Book, Author, Genre


# Create your views here.
@login_required
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', context={'books': books})

@login_required
def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', context={'book': book})

@login_required
def author(request):
    autores = Author.objects.all()
    return render(request, "books/autores.html", context={"autores": autores})

@login_required
def author_detail(request, author_id):
    autor = get_object_or_404(Author, pk=author_id)
    libros = Book.objects.filter(authors=autor)
    return render(request, template_name="books/autordetail.html", context={"autor": autor, "libros": libros})

@login_required
def genre(request):
    generos = Genre.objects.all()
    libros_terror = Book.objects.filter(genre = 1)
    cont_t = 0
    for i in libros_terror:
        cont_t+=1
    libros_comedia = Book.objects.filter(genre = 2)
    cont_c = 0
    for i in libros_comedia:
        cont_c+=1
    libros_deportes = Book.objects.filter(genre = 3)
    cont_d = 0
    for i in libros_deportes:
        cont_d+=1
    return render(request, template_name="books/generos.html", context={"generos": generos, "libros_terror": cont_t, "libros_deportes": cont_d, "libros_comedia": cont_c})

@login_required
def genre_detail(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)
    libros = Book.objects.filter(genre=genre)
    return render(request, template_name="books/librosgen.html", context={"genre": genre, "libros": libros})

@login_required
def form(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        birth_date = request.POST["birth_date"]

        new_author = Author(first_name=first_name, last_name=last_name, birth_date=birth_date)
        new_author.save()

        return render(request, template_name="books/formulario.html", context={"añadido": "Nuevo autor añadido"})


    return render(request, template_name="books/formulario.html")

@login_required
def form2(request):
    autores = Author.objects.all()
    genres = Genre.objects.all()
    if request.method == "POST":
        title = request.POST["title"]
        author_id = request.POST["authors"]
        genre = request.POST["genre"]
        publish_date = request.POST["publish_date"]
        sumary = request.POST["sumary"]


        author = get_object_or_404(Author, id=author_id)
        genre = get_object_or_404(Genre, id=genre)


        new_book = Book(
            title=title,
            authors=author,
            genre=genre,
            publish_date=publish_date,
            sumary=sumary
        )
        new_book.save()

        return render(request, "books/formulario2.html", {
            "añadido": "Nuevo libro añadido a la lista",
            "autores": autores,
            "genres": genres,
        })

    return render(request, "books/formulario2.html", {"autores": autores, "genres": genres})

@login_required
def recientes(request):
    libros = Book.objects.order_by("-publish_date")[:5]
    return render(request, template_name="books/recientes.html", context={"libros": libros})

def jonatan(request):
    return render(request, template_name="books/jonatan.html")

