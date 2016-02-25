from __future__ import unicode_literals

from django.db import models

class SiteModel(models.Model):
    name = models.CharField(max_length=250, null=True)
    state = models.CharField(max_length=250, null=True)
    installation = models.CharField(max_length=250, null=True)
    drainage = models.CharField(max_length=250, null=True)
    mountain_range = models.CharField(max_length=250, null=True)

    def getSiteNames(self):
        sites = SiteModel.objects.values('name')
        
        unique_names = [site['name'].encode('utf-8') for site in sites]


        # unique_names = 'blah'
        return unique_names

    def getSitesTree(self):
    	sites = SiteModel.objects.values('name', 'drainage')

    	sitesTree = {site['drainage'].encode('utf-8'): [] for site in sites}

    	for site in sites:
    		sitesTree[site['drainage'].encode('utf-8')].append(site['name'].encode('utf-8'))

    	return sitesTree