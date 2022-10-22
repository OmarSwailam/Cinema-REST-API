from django.urls import path
from . import views

urlpatterns = [
    path("fbv_list", views.fbv_list, name="fbv_list"),
    path("fbv_pk/<int:pk>", views.fbv_pk, name="fbv_pk"),
    path("cbv_list", views.CbvList.as_view(), name="cbv_list"),
    path("cbv_pk/<int:pk>", views.CbvPk.as_view(), name="cbv_pk"),
]