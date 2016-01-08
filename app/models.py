from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Species(models.Model):
    # bug_id = models.IntegerField()
    state = models.CharField(max_length=150)
    drainage = models.CharField(max_length=150)
