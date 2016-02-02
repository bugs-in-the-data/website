from __future__ import unicode_literals

from django.db import models
from site import SiteModel

class SampleModel(models.Model):
    site = models.ForeignKey(SiteModel, on_delete=models.SET_NULL, null=True)
    sample_name = models.CharField(max_length=250, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    subsite = models.IntegerField(null=True)
    microhabitat = models.CharField(max_length=250, null=True)
    sample_hydro = models.CharField(max_length=250, null=True)
    habitat_size = models.CharField(max_length=250, null=True)
    zone = models.CharField(max_length=250, null=True)
    utm_easting = models.CharField(max_length=250, null=True)
    utm_northing = models.CharField(max_length=250, null=True)
