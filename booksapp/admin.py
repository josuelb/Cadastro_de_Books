from django.contrib import admin
from .models import Book
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'release_year', 'state')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'author')


admin.site.register(Book, BooksAdmin)
