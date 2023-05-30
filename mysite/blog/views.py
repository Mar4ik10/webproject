from django.shortcuts import render
from . import models

# Create your views here.


def home(request):
    queryset = models.HomeModel.objects.first()
    print(queryset.img)
    return render(request, 'index.html', {"home": queryset})


def portfolio(request):
    query = models.PortfolioModel.objects.all()
    return render(request, 'portfolio.html', {"portfolios": query})


def blog(request):
    query = models.BlogModel.objects.all()
    return render(request, 'blog.html', {"posts": query})


def blog_detail(request, pk):
    query = models.BlogModel.objects.get(pk=pk)
    return render(request, 'blogdetail.html', {'blog': query})
