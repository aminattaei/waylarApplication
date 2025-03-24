from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("articles", views.ArticleListViewSet)


urlpatterns = [
    path("", views.BlogListView.as_view(), name="Blog_list"),
    path("<int:pk>/", views.Post_Detail, name="Blog_detail"),
    path("api/", include(router.urls)),
    path("create_new_post/", views.Create_new_post.as_view(), name="create_new_post"),
]
