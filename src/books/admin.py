from django.contrib import admin
from .models import BookTitle, Book
# Register your models here.

admin.site.register(Book)
admin.site.register(BookTitle)