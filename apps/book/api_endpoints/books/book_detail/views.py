from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.book.api_endpoints.books.book_detail.serializers import BooksDetailSerializer
from apps.book.models import Books


class BooksDetailView(APIView):
    def get(self,request, pk):
        book = get_object_or_404(Books, id=pk)
        serializer = BooksDetailSerializer(book)
        return Response(serializer.data)
    
__all__ = ['BooksDetailView']
