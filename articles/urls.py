
from django.urls import path, include
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.articlesList,name="list"),
    path('<slug>',views.article_detail ,name="detail")
]

