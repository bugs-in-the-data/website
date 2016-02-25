from __future__ import unicode_literals

from django.db import models
from django.db.models import Count
from django.core import serializers
from sample import SampleModel
from pprint import pprint
import json

class SubsampleModel(models.Model):
    sample = models.ForeignKey(SampleModel, on_delete=models.SET_NULL, null=True)
    order_name = models.CharField(max_length=250, null=True)
    family = models.CharField(max_length=250, null=True)
    genus = models.CharField(max_length=250, null=True)
    sub_genus = models.CharField(max_length=250, null=True)
    species = models.CharField(max_length=250, null=True)
    taxa = models.CharField(max_length=250, null=True)
    total_count = models.IntegerField(null=True)

    def getPieChartData(self):
        data = []
        uniqueOrders = SubsampleModel.objects.values('order_name').annotate(order_count=Count('order_name'))
        for u in uniqueOrders:
            data.append([u["order_name"].encode("utf-8"), u["order_count"]])

        return data

    def getStackedBarChartData(self):
        data = []
        ordersBySite = SubsampleModel.objects.select_related('sample__site').values('sample__site__name', 'order_name').annotate(order_count=Count('order_name'))

        ## NOTE: debugging
        for o in ordersBySite:
            print o
            # print(o.sample.site.name)
            # print o["order_name"].encode("utf-8")

        return data

    def getTaxaTree(self):
        entries = SubsampleModel.objects.values('order_name', 'family', 'genus', 'species')[:100]

        taxa_tree = {}
        for entry in entries:
            taxa_tree[_get_field(entry, 'order_name')] = {}

        for entry in entries:
            taxa_tree[_get_field(entry, 'order_name')][_get_field(entry, 'family')] = {}

        for entry in entries:
            taxa_tree[_get_field(entry, 'order_name')][_get_field(entry, 'family')][_get_field(entry, 'genus')] = []

        for entry in entries:
            taxa_tree[_get_field(entry, 'order_name')][_get_field(entry, 'family')][_get_field(entry, 'genus')].append(_get_field(entry, 'species'))


        return taxa_tree

def _get_field(entry, field):
    return entry[field].encode('utf-8')
