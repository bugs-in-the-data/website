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
    latitude = models.CharField(max_length=250, null=True)
    longitude = models.CharField(max_length=250, null=True)
	
    def getAllSamples(self, filterHelper):
        data = []
        samples = SampleModel.objects.values('sample_name', 'latitude', 'longitude')
        samples = filterHelper.refineSampleQuery(samples)

        for s in samples:
            if s["latitude"] == None or s["longitude"] == None:
                continue
            name = s["sample_name"].encode("utf-8")
            lat = s["latitude"].encode("utf-8")
            long = s["longitude"].encode("utf-8")
            
            data.append([name, lat, long])
        
        return data

    def getSitesTree(self):
        # entries = SampleModel.objects.values('site__state', 'site__drainage', 'site__name', 'sample_name')
        entries = SampleModel.objects.select_related('site').values('site__state', 'site__drainage', 'site__name', 'sample_name')

        sites_tree = {}
        for entry in entries:
            sites_tree[_get_field(entry, 'site__state')] = {}

        for entry in entries:
            sites_tree[_get_field(entry, 'site__state')][_get_field(entry, 'site__drainage')] = {}

        for entry in entries:
            sites_tree[_get_field(entry, 'site__state')][_get_field(entry, 'site__drainage')][_get_field(entry, 'site__name')] = []

        for entry in entries:
            sites_tree[_get_field(entry, 'site__state')][_get_field(entry, 'site__drainage')][_get_field(entry, 'site__name')].append(_get_field(entry, 'sample_name'))

        return sites_tree

def _get_field(entry, field):
    return entry[field].encode('utf-8')