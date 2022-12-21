from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    short_description = models.CharField(max_length=300)

    def __str__(self):
        return f'post with id {self.id}, title: {self.title}, short description: {self.short_description}'


class Comment(models.Model):
    comment_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'comment from {self.author} for post id {self.post.id}'
