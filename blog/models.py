from django.db import models
from PIL import Image

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=140)
    photo = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

