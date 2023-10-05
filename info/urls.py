
from django.urls import path
from . import views
# from .views import info_index

app_name = "info"
urlpatterns = [
    # path('', views.info_index, name="info_index"),
    path('', views.ShopIndecView.as_view(), name="info_index"),
    # path("groups/", views.groups_list, name="groups_list"),
    path("groups/", views.GroupsListView.as_view(), name="groups_list"),
    # path("products/", views.products_list, name="products_list"),
    path("products/", views.ProductsListView.as_view(), name="products_list"),
    path("products/create", views.create_product, name="create_product"),
    path("products/<int:pk>/", views.ProductDetailsView.as_view(), name="product_details"),
    path("orders/", views.orders_list, name="orders_list"),

]