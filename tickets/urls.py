from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('guests', views.viewsets_guest)
router.register('movies', views.viewsets_movie)
router.register('reservations', views.viewsets_reservation)

urlpatterns = [
    path("no_rest", views.no_rest, name="no_rest"),
    path("fbv_list", views.fbv_list, name="fbv_list"),
    path("fbv_pk/<int:pk>", views.fbv_pk, name="fbv_pk"),
    path("cbv_list", views.CbvList.as_view(), name="cbv_list"),
    path("cbv_pk/<int:pk>", views.CbvPk.as_view(), name="cbv_pk"),
    path("generics_list", views.generics_list.as_view(), name="generics_list"),
    path("generics_pk/<int:pk>", views.generics_pk.as_view(), name="generics_pk"),
    path("viewsets", include(router.urls)),
    path("find_movie", views.find_movie, name='find_movie'),
    path("new_reservation", views.new_reservation, name='new_reservation'),
    path('api-auth', include('rest_framework.urls')),
    path('api-token-auth', obtain_auth_token)
]