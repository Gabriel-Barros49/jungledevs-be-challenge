from django.db import models
from topics.models import Topic


class Post(models.Model):

    title = models.TextField(max_length=50)
    content = models.TextField(max_length=200)
    author = models.ForeignKey(to='accounts.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    topic = models.ForeignKey(to='topics.Topic', on_delete=models.CASCADE)

    def __str__(self):
        return f'Post: {self.title}, id: {self.id}, Topic: {self.topic}'

