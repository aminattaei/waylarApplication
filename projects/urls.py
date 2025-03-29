from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"all", views.ProjectListApiViewSet)

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="projects_list"),
    path("<int:pk>/", views.ProjectDetailView.as_view(), name="Project_detail"),
    path("api/", include(router.urls)),
    path(
        "create_new_article/",
        views.Create_new_project.as_view(),
        name="Create_new_project",
    ),
]
