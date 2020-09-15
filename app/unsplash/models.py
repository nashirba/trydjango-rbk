from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=150)
    image = models.URLField(max_length=250)
    description = models.TextField()
    author_created_date = models.DateTimeField()
    user_saved_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'photo by {self.author} saved by {self.user}'
