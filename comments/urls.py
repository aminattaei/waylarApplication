from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.CommentViewSet)

urlpatterns = [
    path("", views.CommentListView.as_view(), name="comments_list"),
    path("api/", include(router.urls)),
]
