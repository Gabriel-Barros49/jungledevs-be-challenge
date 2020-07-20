from django.db import models
from posts.models import Post


class Comment(models.Model):

    title = models.TextField(max_length=50)
    content = models.TextField(max_length=200)
    author = models.ForeignKey(to='accounts.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    post = models.ForeignKey(to='posts.Post', on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.post}, comment_id: {self.id}'
