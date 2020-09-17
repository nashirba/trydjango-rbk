from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    users = models.ManyToManyField(User)
    author = models.CharField(max_length=150)
    image = models.URLField(max_length=250)
    description = models.TextField()
    user_saved_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['author']

    def __str__(self):
        return f'photo by {self.author} saved by {self.user}'
