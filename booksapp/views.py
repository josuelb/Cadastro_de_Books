from rest_framework import viewsets
from .api.serializer import BookSerializer
from .models import Book
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class BooksViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Book.objects.all()
    serializer_class = BookSerializer
