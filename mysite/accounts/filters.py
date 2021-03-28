import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
    # gte = Greter Than and Equal to  // gt = Greater Than // lte = Less Than and Equal to // lt = Less Than
    # icontains = ignore case sensitivity (Make case insensitive)
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    note = CharFilter(field_name='note', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
