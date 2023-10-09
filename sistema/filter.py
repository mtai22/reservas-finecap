import django_filters

from .models import Reserva


class ReservaFilter(django_filters.FilterSet):
    cnpj = django_filters.CharFilter()
    nome_empresa = django_filters.CharFilter()
    categoria_empresa = django_filters.CharFilter()
    quitado = django_filters.BooleanFilter()
    data = django_filters.DateTimeFilter()
    stand__valor = django_filters.BooleanFilter()


    class Meta:
        model = Reserva
        fields = ('cnpj', 'nome_empresa', 'categoria_empresa', 'quitado', 'data', )