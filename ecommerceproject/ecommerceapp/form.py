import django_filters
from django.forms import forms

from ecommerceapp.models import Product


class ProductFilter(forms.Form):
    # price = django_filters.NumberFilter()
    # price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    # price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    price__gt = forms.IntegerField()
    price__lt = forms.IntegerField()
    class Meta:
        model = Product
        fields = {
            'price': ['lt', 'gt']

        }