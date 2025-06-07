from django.urls import path
from .views import BookTitleListView, book_title_detail

app_name = 'books'

urlpatterns = [
    path('', BookTitleListView.as_view(), {'letter': None}, name='main'),
    path('<str:letter>/', BookTitleListView.as_view(), name='main'),
    path('<pk>/', book_title_detail, name='detail'),
]
