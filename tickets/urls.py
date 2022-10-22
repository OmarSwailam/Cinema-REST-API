from django.urls import path
from . import views

urlpatterns = [
    path("list", views.fbv_list, name="fbv_list"),
    path("pk/<int:pk>", views.fbv_pk, name="fbv_pk")
]