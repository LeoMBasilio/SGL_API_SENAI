from .serializers import LivrosSerializers, LocacoesSerializer, UsuariosSerializers
from .models import Livros, usuarios, locacao
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class LivrosViewSets(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset= Livros.objects.all()
    serializer_class = LivrosSerializers

class UsuariosViewSets(viewsets.ModelViewSet):
    queryset = usuarios.objects.all()
    serializer_class = UsuariosSerializers

class LocacoesViewSet(viewsets.ModelViewSet):
    queryset = locacao
    serializer_class = LocacoesSerializer