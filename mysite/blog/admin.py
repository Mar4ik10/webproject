from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.BlogModel)
admin.site.register(models.HomeModel)
admin.site.register(models.PortfolioModel)
