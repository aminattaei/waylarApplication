from django.views import generic
from .models import Comment

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CommentSerializer


class CommentListView(generic.ListView):
    template_name = "comments/Comment_List.html"
    model = Comment
    context_object_name = "comments"


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
