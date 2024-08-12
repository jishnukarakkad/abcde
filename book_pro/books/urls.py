from django.urls import path
from .views import BookListCreate, BookRetrieveUpdateDestroy

urlpatterns = [
    path('book/', BookListCreate.as_view(), name='book-list-create'),
    path('book/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
]
