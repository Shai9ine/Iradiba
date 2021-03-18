from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='articles/')
    body = RichTextUploadingField(null=True, blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/articles/{self.id}/{self.title.replace(' ', '-')}"
