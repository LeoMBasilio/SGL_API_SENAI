from .serializers import LivrosSerializers, LocacoesSerializer, UsuariosSerializers
from .models import Livros, usuarios, locacao
from rest_framework import viewsets

class LivrosViewSets(viewsets.ModelViewSet):
    queryset= Livros.objects.all()
    serializer_class = LivrosSerializers

class UsuariosViewSets(viewsets.ModelViewSet):
    queryset = usuarios.objects.all()
    serializer_class = UsuariosSerializers

class LocacoesViewSet(viewsets.ModelViewSet):
    queryset = locacao
    serializer_class = LocacoesSerializer