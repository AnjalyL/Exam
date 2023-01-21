from django.shortcuts import render
from ecommerceapp.models import Product
from django.db.models import Q

def searchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request, 'search.html',{'query' : query,'products':products})


def sort(request):
    products = None
    query = None
    query1 = None
    if 'q' in request.GET and 'p' in request.GET:
        query = request.GET.get('q')
        query1 = request.GET.get('p')
        products = Product.objects.all().filter(Q(Product.price>=query) | Q(Product.price<=query1))

    return render(request, 'sort.html',{'products': products})
