from . import views
from django.urls import path
# from .views import process_get_view

app_name = "map_data"
urlpatterns = [
    path("get/", views.process_get_view, name="process_get_view"),
    path("bio/", views.user_form, name="user-form"),
    path("upload/", views.hundle_file_upload, name="file-upload"),
]