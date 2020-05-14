from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=100)
    post=models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
