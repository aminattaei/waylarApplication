from django.shortcuts import render
from .models import ContactUs
from .forms import ContactUsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy



class ContactFormView(LoginRequiredMixin, generic.CreateView):
    model = ContactUs
    template_name = "ContactUs/contact-us.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("contact_done")

    def form_valid(self, form):
        form.instance.email = self.request.user.email
        return super().form_valid(form)


class ContactFormViewDone(LoginRequiredMixin, generic.TemplateView):
    template_name = "ContactUs/contact-done.html"
