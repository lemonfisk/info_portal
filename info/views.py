from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpRequest
from timeit import default_timer
from django.contrib.auth.models import Group
from django.views.generic import TemplateView, ListView, DetailView

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


class ProductDetailsView(DetailView):
    template_name = "info/product-details.html"
    model = Product
    context_object_name = "product"

class ProductsListView(ListView):
    template_name = "info/products-list.html"
    model = Product
    context_object_name = "products"


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


class OrdersListView(ListView):
    queryset = (
        Order.objects.select_related("user").prefetch_related('products')
    )

class OrdersDetailView(DetailView):
    queryset = (
        Order.objects.select_related("user").prefetch_related('products')
    )

