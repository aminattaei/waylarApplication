from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_user_account, name="login_user_account"),
    path("register/", views.register_user_account, name="register_user_account"),
    path("logout/", views.logout_view, name="logout"),  
    path("logout/done/", views.LogOutDoneView.as_view, name="logout_done"),
    path("profile/", views.profile, name="profile"),
]
