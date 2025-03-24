from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls")),
    path("articles/", include("article.urls")),
    path("services/", include("services.urls")),
    path("contact-us/", include("ContactUs.urls")),
    path("comments/", include("comments.urls")),
    path("", include("IndexPage.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
