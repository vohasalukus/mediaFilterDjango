from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="category")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    photo = models.ImageField(upload_to="author")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books_category')
    author = models.ManyToManyField(Author, related_name='books_author')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
