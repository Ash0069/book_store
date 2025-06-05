from django.urls import path
from .views import book_title_view_list, book_title_detail

app_name = 'books'

urlpatterns = [
    path('', book_title_view_list, name='main'),
    path('<pk>/', book_title_detail, name='detail'),
]
