from django.http import HttpResponse
from django.shortcuts import render
from customers.models import Customer
from books.models import Book, BookTitle

def home_view(request):
    qs = Customer.objects.all()
    obj = BookTitle.objects.get(id=1)
    books = obj.books
    print(books)
    context = {
        'qs' : qs,
        'obj' : obj,
    }
    return render(request, 'main.html', context)