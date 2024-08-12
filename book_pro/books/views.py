from rest_framework import generics
from .models import book
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializer
