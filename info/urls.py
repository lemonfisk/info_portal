
from django.urls import path
from . import views
# from .views import info_index

app_name = "info"
urlpatterns = [
    path('', views.info_index, name="info_index"),
    path("groups/", views.groups_list, name="groups_list"),
    path("products/", views.products_list, name="products_list"),
    path("orders/", views.orders_list, name="orders_list"),
]