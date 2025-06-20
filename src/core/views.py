from django.http import HttpResponseRedirect
from django.shortcuts import render
from customers.models import Customer
from books.models import Book, BookTitle

def change_theme(request):
    if 'is_dark_mode' in request.session:
        request.session['is_dark_mode'] = not request.session['is_dark_mode']
    else:
        request.session['is_dark_mode'] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

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