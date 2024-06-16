from django.contrib import admin
from .models import Category, Author, Book


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
