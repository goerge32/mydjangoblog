
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.articlesList),
    path('slug',views.article_detail)
]

