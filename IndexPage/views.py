from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from projects.models import Project
from article.models import Blog
from services.models import Service
from comments.models import Comment
from .models import NewsPaper


class HomeProjectListView(generic.ListView):
    template_name = "IndexPage/index.html"
    context_object_name = "projects"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blog.objects.order_by("-created_time").all
        context["services"] = Service.objects.all()
        context["comments"] = Comment.objects.filter(is_approved=True)
        return context


class FaqTemplateView(generic.TemplateView):
    template_name = "faq/faq.html"


class NewsPaperCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "partials/_footer.html"
    model = NewsPaper
    success_url = reverse_lazy("indexpage:home_index")
    fields = ["email"]

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "ایمیل شما با موفقیت ثبت شد")
        return response


def Search_bar(request):
    query = request.GET.get("q", "").strip()
    if not query:
        messages.error(request, "لطفا یک عبارت برای جستجو وارد کنید")
        return render(request, "IndexPage/result_search.html", context={"query": query})
    try:
        result = Project.objects.filter(title__icontains=query)
        result |= Blog.objects.filter(title__icontains=query)
    except Exception as e:
        messages.error(request, "خطایی در انجام جستجو رخ داده است")
        result = []
        

    context = {"query": query, "result": result}
    return render(request, "IndexPage/result_search.html", context=context)
