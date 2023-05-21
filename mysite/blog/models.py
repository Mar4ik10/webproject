from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class HomeModel(models.Model):
    title = models.CharField(max_length=100)
    text = RichTextField()

    def __str__(self):
        return self.title


class BlogModel(models.Model):
    title = models.CharField(max_length=254)
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    text = RichTextField()
    img = models.ImageField(upload_to='public/')

    def __str__(self):
        return self.title


class AboutModel(models.Model):
    title = models.CharField(max_length=64)
    text = RichTextField()

    def __str__(self):
        return self.title


class AboutUrlsModel(models.Model):
    ICON_CHOICES = [("instagram", "Instagram"), ("youtube", "YouTube"), ("telegram", "Telegram"), ("github", "GitHub"), ("twitter", "Twitter")]
    
    name = models.CharField(max_length=64)
    url = models.URLField(max_length=200)
    icons = models.CharField(max_length=64, choices=ICON_CHOICES)

    def __str__(self):
        return self.name
