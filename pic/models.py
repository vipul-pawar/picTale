from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to='myimages/')
    image = models.ImageField(upload_to='myimages/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='myvideos/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title