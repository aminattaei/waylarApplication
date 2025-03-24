from django.shortcuts import render, get_object_or_404
from .models import Blog
from comments.models import Comment
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import CommentForm

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleSerializer


class BlogListView(generic.ListView):
    template_name = "articles/blog.html"
    context_object_name = "articles"
    model = Blog
    paginate_by = 2



class ArticleListViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


@login_required(login_url="/accounts/login/")
def Post_Detail(request, pk):
    post = get_object_or_404(Blog, id=pk)
    comments = Comment.objects.filter(post=post, is_approved=True)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.content = form.cleaned_data["content"]
            new_comment.is_approved = False
            new_comment.save()

            messages.success(
                request, "نظر شما ارسال شد و پس از تأیید مدیر منتشر خواهد شد."
            )
            return HttpResponseRedirect(request.path_info)

    context = {"form": form, "comments": comments, "post": post}
    return render(request, "articles/single-blog.html", context=context)
