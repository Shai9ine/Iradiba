from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='articles/')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/articles/{self.id}/{self.title.replace(' ', '-')}"
