
from . import views
from django.urls import path
from django_filters.views import FilterView, object_filter

from .models import Product

app_name = 'ecommerceapp'
urlpatterns = [

    path('',views.allProdCat,name = 'allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name = 'products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name = 'prodCatdetail'),

]
