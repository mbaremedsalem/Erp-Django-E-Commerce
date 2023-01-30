import django_filters
from .models import Product

class ShopFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category',]
        # exclude = ['slug','experience','image','prix']