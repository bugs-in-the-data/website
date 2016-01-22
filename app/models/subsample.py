from __future__ import unicode_literals

from django.db import models
from sample import SampleModel

class SubsampleModel(models.Model):
    sample = models.ForeignKey(SampleModel, on_delete=models.SET_NULL, null=True)
    order = models.CharField(max_length=250, null=True)
    family = models.CharField(max_length=250, null=True)
    genus = models.CharField(max_length=250, null=True)
    sub_genus = models.CharField(max_length=250, null=True)
    species = models.CharField(max_length=250, null=True)
    taxa = models.CharField(max_length=250, null=True)
    count = models.IntegerField(null=True)
    percent_subsample = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    total_count = models.IntegerField(null=True)
    comment = models.TextField(null=True)

    def getData(self):
        test = {
            'name': 'Ty'
        }
        return test
