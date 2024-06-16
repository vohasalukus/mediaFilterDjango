from django.urls import path
from .views import home, books_by_category, books_by_author

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>/', books_by_category, name='books_by_category'),
    path('author/<slug:slug>/', books_by_author, name='books_by_author'),
]
