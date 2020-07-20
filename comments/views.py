from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = None
    serializer_class = CommentSerializer

    def filter_queryset(self, queryset):


        parent_post = self.kwargs.get('post_pk')
        return queryset.filter(post__id=parent_post)


