import django_filters
from .models import Address, City

from django_filters import FilterSet


class AddressFilter(django_filters.FilterSet):
    city = django_filters.ModelChoiceFilter(
        queryset=City.objects.all())
    class Meta:
        model = Address
        fields = '__all__'




