from django.urls import path
from apps.book.api_endpoints.books.book_list.views import BookListView
from apps.book.api_endpoints.books.book_detail.views import BooksDetailView
from apps.book.api_endpoints.user.user_list.views import CustomUserListView
from apps.book.api_endpoints.user.user_detail.views import CustomUserDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BooksDetailView.as_view(), name='book-detail'),
    path('user/', CustomUserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
]
