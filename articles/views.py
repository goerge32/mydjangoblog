from django.shortcuts import render,HttpResponse
from . import models
# Create your views here.
def articlesList(request):
    articles = models.Article.objects.all().order_by('date')

    return render(request, 'articles/articleslist.html',{'articles':articles})
    
def article_datail(request, slug):
    return HttpResponse(slug)