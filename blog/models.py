from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    text = models.TextField(max_length=500, blank=False, null=False)
