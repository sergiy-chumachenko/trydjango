from django.db import models
from django.shortcuts import reverse


class Course(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)

    def get_absolute_url(self):
        return reverse('courses:course-detail', kwargs={'id': self.id})
