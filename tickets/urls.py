from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('guests', views.viewsets_guest)
router.register('movies', views.viewsets_movie)
router.register('reservations', views.viewsets_reservation)

urlpatterns = [
    path("fbv_list", views.fbv_list, name="fbv_list"),
    path("fbv_pk/<int:pk>", views.fbv_pk, name="fbv_pk"),
    path("cbv_list", views.CbvList.as_view(), name="cbv_list"),
    path("cbv_pk/<int:pk>", views.CbvPk.as_view(), name="cbv_pk"),
    path("viewsets>", include(router.urls)),
]