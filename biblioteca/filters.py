import django_filters
from .models import Livros

class LivrosFilter(django_filters.FilterSet):
    ano_antes = django_filters.DateFilter(field_name='ano_publicacao', lookup_expr='lte')
    ano_apos = django_filters.DateFilter(field_name='ano_publicacao', lookup_expr='gte')

    class Meta:
        model = Livros
        fields = ['titulo', 'ano_antes', 'ano_apos']