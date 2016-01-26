from __future__ import unicode_literals

from django.db import models

class SiteModel(models.Model):
    state = models.CharField(max_length=250, null=True)
    installation = models.CharField(max_length=250, null=True)
    drainage = models.CharField(max_length=250, null=True)
    mountain_range = models.CharField(max_length=250, null=True)