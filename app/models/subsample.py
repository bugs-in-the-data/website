from __future__ import unicode_literals

from django.db import models
from django.db.models import Count
from django.core import serializers
from sample import SampleModel
from pprint import pprint
from collections import Counter
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
        ordersBySite = SubsampleModel.objects.select_related('sample__site').values('sample__site__name', 'order_name').annotate(order_count=Count('order_name'))

        seen = []
        sites = []
        temp = {}
        for o in ordersBySite:
            order = o["order_name"].encode("utf-8")
            site = o["sample__site__name"].encode("utf-8")
            count = o["order_count"]

            if order not in seen:
                seen.append(order)
                temp[order] = {}
            if site not in sites:
                sites.append(site)

            temp[order][site] = count
        sites = sorted(sites)
        sites.insert(0, 'x'.encode("utf-8"))

        data = []
        data.append(sites)
        for key, val in temp.iteritems():
            row = [key]
            for site in sites:
                if site in temp[key]:
                    row.append(temp[key][site])
                else:
                    row.append(0)
            data.append(row)

        return data
