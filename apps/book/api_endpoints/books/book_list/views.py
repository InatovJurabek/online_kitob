from rest_framework import generics
from apps.book.models import Books
from .serializers import BookListSerializer

class BookListView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookListSerializer
    