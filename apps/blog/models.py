from django.contrib.auth.models import User
from django.db import models
from apps.products.models import Category


# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    author_name = models.CharField(max_length=255)
    author_image = models.ImageField(upload_to='author')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
