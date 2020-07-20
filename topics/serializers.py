from rest_framework import serializers

from topics.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Topic
        fields ='__all__'
