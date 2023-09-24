from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from timeit import default_timer
from django.contrib.auth.models import Group
from .models import Product, Order


def info_index(request: HttpRequest):
    products = [
        ('laptop', 1999),
        ('Desc', 299),
        ('Smartphone', 4564),
    ]
    context = {
        "time_running": default_timer(),
        "products": products,

    }
    # return HttpResponse("dgdfgdfgdfgdfg")
    return render(request, 'info/info-st.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'info/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'info/products-list.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related('products').all(),
    }
    return render(request, 'info/orders-list.html', context=context)
