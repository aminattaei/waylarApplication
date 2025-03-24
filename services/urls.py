from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.ServicesViewSet)
urlpatterns = [
    path("", views.ServicesListView.as_view(), name="services_list"),
    path("api/", include(router.urls)),
]
