from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpRequest
from timeit import default_timer
from django.contrib.auth.models import Group
from .models import Product, Order
# from .forms import ProductForm
from .forms import GroupForm
from django.views import View


class ShopIndecView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products = [
            ('laptop', 1999),
            ('Desc', 299),
            ('Smartphone', 4564),
        ]
        context = {
            "time_running": default_timer(),
            "products": products,

        }
        return render(request, 'info/info-st.html', context=context)


# def info_index(request: HttpRequest):
#     products = [
#         ('laptop', 1999),
#         ('Desc', 299),
#         ('Smartphone', 4564),
#     ]
#     context = {
#         "time_running": default_timer(),
#         "products": products,
#
#     }
#     # return HttpResponse("dgdfgdfgdfgdfg")
#     return render(request, 'info/info-st.html', context=context)

class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": GroupForm,
            "groups": Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, 'info/groups-list.html', context=context)

    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)

# def groups_list(request: HttpRequest):
#     context = {
#         "groups": Group.objects.prefetch_related('permissions').all(),
#     }
#     return render(request, 'info/groups-list.html', context=context)

class ProductDetailsView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:

        product = get_object_or_404(Product, pk=pk)
        context = {
            "product": product,
        }
        return render(request, 'info/product-details.html', context=context)

def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'info/products-list.html', context=context)


def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data["name"]
            # price = form.cleaned_data["price"]
            # Product.objects.create(**form.cleaned_data)
            form.save()
            url = reverse("info:products_list")
            return redirect(url)
    else:
        form = ProductForm()
    context = {
        "form": form,
    }

    return render(request, 'info/create-product.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related('products').all(),
    }
    return render(request, 'info/orders-list.html', context=context)
