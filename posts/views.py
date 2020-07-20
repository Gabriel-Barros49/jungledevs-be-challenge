
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):

    queryset =Post.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = None
    serializer_class = PostSerializer


    def filter_queryset(self, queryset):

        parent_topic = self.kwargs.get('topic_url_name')
        return queryset.filter(topic__url_name=parent_topic)





