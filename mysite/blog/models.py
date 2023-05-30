from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class HomeModel(models.Model):
    title = models.CharField(max_length=100)
    text = RichTextField()
    img = models.ImageField(upload_to='public/')

    def __str__(self):
        return self.title


class BlogModel(models.Model):
    title = models.CharField(max_length=254)
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    text = RichTextField()
    img = models.ImageField(upload_to='public/')

    def __str__(self):
        return self.title


class PortfolioModel(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    url = models.URLField(max_length=200)
    img = models.ImageField(upload_to='public/')

    def __str__(self):
        return self.title
