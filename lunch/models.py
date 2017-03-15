from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    key = models.CharField(max_length=25)
    office = models.CharField(max_length=200)
    radius = models.CharField(max_length=5)

    def __str__(self):
        return self.name
