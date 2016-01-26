from __future__ import unicode_literals

from django.db import models
from site import SiteModel

class SampleModel(models.Model):
    site = models.ForeignKey(SiteModel, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    subsite = models.IntegerField(null=True)
    microhabitat = models.CharField(max_length=250, null=True)
    sample_hydro = models.CharField(max_length=250, null=True)
    habitat_size = models.CharField(max_length=250, null=True)
    pool_area = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    pool_area = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    riff_area = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    canopy_upstream = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    canopy_left = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    canopy_downstream = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    average_canopy_cover = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    total_canopy_cover = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    bedrock = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    cobble = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    gravel = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    silt = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    travertine = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    sand = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    algae = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    macrophite = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    moss = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    detritus = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    temperature = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    disolved_oxygen = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    ph = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    conductivity = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    grazing_impact = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    collection_comments = models.TextField(null=True)
    habitat_comments = models.TextField(null=True)
    collector = models.CharField(max_length=250, null=True)
    zone = models.CharField(max_length=250, null=True)
    utm_easting = models.CharField(max_length=250, null=True)
    utm_northing = models.CharField(max_length=250, null=True)