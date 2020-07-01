from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def preview(self):
        return self.body[:50] + "..."
