from django.shortcuts import render, get_object_or_404
from .models import Category, Author, Book


def home(request):
    return render(request=request,
                  template_name='mediaFilter_app/home.html',
                  context={
                      'books': Book.objects.all(),
                      'categories': Category.objects.all(),
                      'authors': Author.objects.all()
                  })


def books_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books_category.all()
    return render(request=request,
                  template_name='mediaFilter_app/home.html',
                  context={
                      'books': books,
                      'categories': Category.objects.all(),
                      'authors': Author.objects.all()
                  })


def books_by_author(request, slug):
    author = get_object_or_404(Author, slug=slug)
    books = author.books_author.all()
    return render(request=request,
                  template_name='mediaFilter_app/home.html',
                  context={
                      'books': books,
                      'authors': Author.objects.all(),
                      'categories': Category.objects.all(),
                  })
