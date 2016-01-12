from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Species(models.Model):
    sample_id = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    drainage = models.CharField(max_length=150)
