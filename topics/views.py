from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from topics.models import Topic
from topics.serializers import TopicSerializer


class TopicViewset(viewsets.ModelViewSet):

    lookup_field = 'url_name'
    pagination_class = None
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        topic_creator = self.request.user
        serializer.save(author=topic_creator)