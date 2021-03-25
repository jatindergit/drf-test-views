from .serializers import BookSerializer
from rest_framework import generics
from .models import Book


class ListCreateBookView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset=Book.objects.all()