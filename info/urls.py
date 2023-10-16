
from django.urls import path
from . import views
# from .views import info_index

app_name = "info"
urlpatterns = [
    path('', views.ShopIndecView.as_view(), name="info_index"),
    path("groups/", views.GroupsListView.as_view(), name="groups_list"),
    path("products/", views.ProductsListView.as_view(), name="products_list"),
    path("products/export", views.ProductsDataExportView.as_view(), name="products-export"),

    path("products/create", views.ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/", views.ProductDetailsView.as_view(), name="product_details"),
    path("products/<int:pk>/update", views.ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/confirm-delete", views.ProductDeleteView.as_view(), name="product_delete"),
    path("orders/", views.OrdersListView.as_view(), name="orders_list"),
    path("orders/<int:pk>/", views.OrdersDetailView.as_view(), name="order_details"),
]