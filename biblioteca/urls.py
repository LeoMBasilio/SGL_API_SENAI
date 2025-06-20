from .views import LivrosViewSets, LocacoesViewSet, UsuariosViewSets, LivrosDataViewSets
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'livro', LivrosViewSets, basename='livro')
router.register(r'usuario', UsuariosViewSets, basename='usuario')
router.register(r'locacao', LocacoesViewSet, basename='locacao')
router.register(r'livrosData', LivrosDataViewSets, basename='livrosData')

urlpatterns = router.urls