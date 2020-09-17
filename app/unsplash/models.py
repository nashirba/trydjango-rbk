from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    users = models.ManyToManyField(User)
    author = models.CharField(max_length=150)
    image = models.URLField(max_length=250)
    description = models.TextField()
    photo_unsplash_id = models.CharField(max_length=50)

    def __str__(self):
        return f'photo by {self.author}'
