from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path("list/", views.list_view, name="list-cars"),
    path("add/", views.add_view, name="add-cars"),
    path("delete/", views.delete_view, name="delete-cars")
]
