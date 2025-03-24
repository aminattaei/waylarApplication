from django.urls import path
from . import views

urlpatterns = [
    path("", views.ContactFormView.as_view(), name="contact_form"),
    path("done/", views.ContactFormViewDone.as_view(), name="contact_done"),
]
