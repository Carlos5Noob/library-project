from django.test import TestCase
from django.utils.timezone import now
from django.urls import reverse

from books.models import Book, Author, Genre

# Create your tests here.

class ModelTests(TestCase):
    def setUp(self):
        self.autor = Author.objects.create(first_name="Henry", last_name="Titi", birth_date=now())
        self.genre = Genre.objects.create(name="Fantasy")
        self.libro = Book.objects.create(title="Chapiadora.com", authors=self.autor, genre=self.genre, publish_date=now(), sumary="kevedo")

    def test_book_creation(self):
        response = self.client.get(reverse("books:index"))
        self.assertContains(response, "Chapiadora.com")

    def test_author_creation(self):
        response = self.client.get(reverse("books:index"))
        self.assertContains(response, "Henry")

    def test_genre_creation(self):
        response = self.client.get(reverse("books:index"))
        self.assertContains(response, 4)

    def test_relation(self):
        self.assertEqual(self.autor, self.libro.authors)

class ViewTests(TestCase):
    def setUp(self):
        self.autor = Author.objects.create(first_name="Henry", last_name="Titi", birth_date=now())
        self.genre = Genre.objects.create(name="Fantasy")
        self.libro = Book.objects.create(title="Chapiadora.com", authors=self.autor, genre=self.genre,
                                         publish_date=now(), sumary="kevedo")

        self.response1 = self.client.get(reverse("books:index"))
        self.response2 = self.client.get(reverse("books:detail", kwargs={"book_id": self.libro.id}))
        self.response3 = self.client.get(reverse("books:author"))
        self.response4 = self.client.get(reverse("books:genero"))

    def test_status(self):
        self.assertEqual(self.response1.status_code, 200)
        self.assertEqual(self.response2.status_code, 200)
        self.assertEqual(self.response3.status_code, 200)
        self.assertEqual(self.response4.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response1, "books/index.html")
        self.assertTemplateUsed(self.response2, "books/detail.html")
        self.assertTemplateUsed(self.response3, "books/autores.html")
        self.assertTemplateUsed(self.response4, "books/generos.html")

class UrlTests(TestCase):
    def setUp(self):
        self.autor = Author.objects.create(first_name="Henry", last_name="Titi", birth_date=now())
        self.genre = Genre.objects.create(name="Fantasy")
        self.libro = Book.objects.create(title="Chapiadora.com", authors=self.autor, genre=self.genre,
                                         publish_date=now(), sumary="kevedo")
    def test_urls(self):
        self.assertURLEqual("/books/", reverse("books:index"))
        self.assertURLEqual("/books/autores/", reverse("books:author"))
        self.assertURLEqual("/books/generos/", reverse("books:genero"))
        self.assertURLEqual("/books/1/", reverse("books:detail", kwargs={"book_id": self.libro.id}))