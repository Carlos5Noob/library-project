from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    publish_date = models.DateTimeField()
    sumary = models.TextField()

    def __str__(self):
        return f"{self.title}"

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"