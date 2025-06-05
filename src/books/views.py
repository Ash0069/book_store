from django.shortcuts import render
from .models import Book, BookTitle

# Create your views here.
def book_title_view_list(request):
    qs = BookTitle.objects.all()
    return render(request, 'books/main.html', { 'qs' : qs })

def book_title_detail(request, **kwargs):
    pk=kwargs.get('pk')
    obj = BookTitle.objects.get(pk=pk)
    return render(request, 'books/details.html', { 'obj' : obj })