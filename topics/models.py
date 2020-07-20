from django.db import models

class Topic(models.Model):

    name = models.TextField(max_length=50)
    title = models.TextField(max_length=50)
    author = models.ForeignKey(to='accounts.User', on_delete=models.CASCADE)
    description = models.TextField(max_length=100)
    url_name = models.SlugField()
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)

    def __str__(self):
        return f'{self.name}'
