from .serializers import LivrosSerializers, LocacoesSerializer, UsuariosSerializers
from .models import Livros, usuarios, locacao
from .filters import LivrosFilter
from .permissions import IsOwnerOfTheObject
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication #
from rest_framework.permissions import IsAuthenticated #
from django_filters.rest_framework import DjangoFilterBackend#

class LivrosViewSets(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication] #
    permission_classes = [IsAuthenticated] #

    queryset= Livros.objects.all()
    serializer_class = LivrosSerializers
    filter_backends = [DjangoFilterBackend]#
    filterset_fields = ['titulo', 'autor']#

class LivrosDataViewSets(viewsets.ModelViewSet):
    queryset= Livros.objects.all()
    serializer_class = LivrosSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = LivrosFilter

class UsuariosViewSets(viewsets.ModelViewSet):
    serializer_class = UsuariosSerializers
    permission_classes = [IsAuthenticated, IsOwnerOfTheObject]

    def get_queryset(self):
        return usuarios.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LocacoesViewSet(viewsets.ModelViewSet):
    queryset = locacao
    serializer_class = LocacoesSerializer