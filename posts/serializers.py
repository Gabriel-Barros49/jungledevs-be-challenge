from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    topic = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = '__all__'