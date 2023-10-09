from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from timeit import default_timer
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

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
    queryset = Product.objects.filter(archived=False)

class ProductsListView(ListView):
    template_name = "info/products-list.html"
    model = Product
    context_object_name = "products"


# def create_product(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             # name = form.cleaned_data["name"]
#             # price = form.cleaned_data["price"]
#             # Product.objects.create(**form.cleaned_data)
#             form.save()
#             url = reverse("info:products_list")
#             return redirect(url)
#     else:
#         form = ProductForm()
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'info/create-product.html', context=context)

class ProductCreateView(CreateView):
    model = Product
    fields = "name", "price", "description", "discount"
    success_url = reverse_lazy('info:products_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = "name", "price", "description", "discount"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            "info:product_details",
            kwargs={"pk": self.object.pk},
        )


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("info:products_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)

class OrdersListView(ListView):
    queryset = (
        Order.objects.select_related("user").prefetch_related('products')
    )

class OrdersDetailView(DetailView):
    queryset = (
        Order.objects.select_related("user").prefetch_related('products')
    )

