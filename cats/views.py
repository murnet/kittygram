from rest_framework import generics

from .models import Cat
from .serializers import CatSerializer


class CatList(generics.ListCreateAPIView):
    # Как сделать, чтобы можно было отпралять список котиков?
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
