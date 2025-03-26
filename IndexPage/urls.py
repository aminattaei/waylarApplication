from django.urls import path
from . import views

app_name = "indexpage"

urlpatterns = [
    path("", views.HomeProjectListView.as_view(), name="home_index"),
    path("faq/", views.FaqTemplateView.as_view(), name="faq_page"),
    path("subscribe/", views.NewsPaperCreateView.as_view(), name="NewsPaper_create"),
    path("search/", views.Search_bar, name="search"),
]
