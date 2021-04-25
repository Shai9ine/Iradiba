from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from account.models import NewUser
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='articles/')
    body = RichTextUploadingField(null=True, blank=True)
    description = models.TextField(default='default text')
    author = models.ForeignKey(NewUser, default=None, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_promote = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.author.first_name} {self.author.last_name}"

    def get_absolute_url(self):
        return f"/articles/{self.id}/{self.title.replace(' ', '-')}"
