from django.db import models
from django.shortcuts import reverse


class Article(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    text = models.TextField(max_length=500, blank=False, null=False)

    def get_absolute_url(self):
        return reverse('articles:article-detail', kwargs={"id": self.id})
