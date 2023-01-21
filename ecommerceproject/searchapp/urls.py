from django.urls import path
from . import views

app_name = 'searchapp'
urlpatterns = [
    path('',views.searchResult,name='searchResult'),
    path('sort',views.sort,name='sort')


]