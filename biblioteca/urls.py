from .views import LivrosViewSets, LocacoesViewSet, UsuariosViewSets
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'livro', LivrosViewSets, basename='livro')
router.register(r'usuario', UsuariosViewSets, basename='usuario')
router.register(r'locacao', LocacoesViewSet, basename='locacao')

urlpatterns = router.urls