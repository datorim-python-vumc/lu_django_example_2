from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=4000)
    time = models.DateTimeField()

