from django.shortcuts import render
from .models import Book, BookTitle
from django.views.generic import ListView, FormView
from .forms import BookTitleForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
import string
# Create your views here.

class BookTitleListView(FormView, ListView):
    # model = BookTitle
    # queryset = BookTitle.objects.all()
    template_name = 'books/main.html'
    context_object_name = 'qs'
    form_class = BookTitleForm
    # success_url = reverse_lazy("books:main")
    # ordering = ('-created',)
    i_instance = None

    def get_success_url(self):
        return self.request.path

    def get_queryset(self):
        parameter = self.kwargs.get('letter') if self.kwargs.get('letter') else 'a'
        return BookTitle.objects.filter(title__startswith=parameter)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        letters = list(string.ascii_uppercase)
        context['letters'] = letters
        context['selected_letter'] = self.kwargs.get('letter') if self.kwargs.get('letter') else 'a'
        return context

    def form_valid(self, form):
        self.i_instance = form.save()
        messages.add_message(self.request, messages.INFO, f"Book Title : {self.i_instance.title} has been created", extra_tags="success")
        return super().form_valid(form)
        # form.save()
        # response = super().form_valid(form)
        # # Inject flag into context
        # self.extra_context = {'success': True}
        # return response
    
    def form_invalid(self, form):
        # self.object_list = self.get_queryset()
        # return super().form_invalid(form)
        self.object_list = self.get_queryset()
        # Optionally, handle specific field errors
        self.extra_context = {'form': form, 'title_error': form['title'].errors}
        return super().form_invalid(form)
    
# def book_title_view_list(request):
#     qs = BookTitle.objects.all()
#     return render(request, 'books/main.html', { 'qs' : qs })

def book_title_detail(request, **kwargs):
    pk=kwargs.get('pk')
    obj = BookTitle.objects.get(pk=pk)
    return render(request, 'books/details.html', { 'obj' : obj })