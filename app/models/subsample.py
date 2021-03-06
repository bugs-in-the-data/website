from __future__ import unicode_literals

from django.db import models
from django.db.models import Count
from django.core import serializers
from sample import SampleModel
from pprint import pprint
from collections import Counter
from app.helpers import FilterHelperModel
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

    def getPieChartData(self, filterHelper):
        data = []
        uniqueOrders = SubsampleModel.objects.values(filterHelper.getSubTaxa()).annotate(taxa_count=Count('species',distinct=True))
        uniqueOrders = filterHelper.refineSubsampleQuery(uniqueOrders)
        for u in uniqueOrders:
            label = u[filterHelper.getSubTaxa()].encode("utf-8")
            count = u["taxa_count"]

            if label == 'NULL':
                continue

            data.append([label, count])
        data = sorted(data, key=lambda a_entry: a_entry[0])
        return data

    def getLineChartData(self, filterHelper):
        ## @NOTE: the query needs to mimic
        ## SELECT y.date, x.order_name, COUNT(x.order_name) as order_count
        ## FROM app_subsamplemodel x
        ## LEFT JOIN app_samplemodel y on x.sample_id = y.id
        ## GROUP BY CONCAT(y.date,x.order_name);

        ordersByDate = SubsampleModel.objects.select_related('sample').values('sample__date', filterHelper.getSubTaxa()).annotate(taxa_count=Count('species'))
        ordersByDate = filterHelper.refineSubsampleQuery(ordersByDate)

        seen = []
        labels = []
        temp = {}
        for o in ordersByDate:
            date = o["sample__date"].strftime("%m-%d-%Y")
            label = o[filterHelper.getSubTaxa()].encode("utf-8")
            count = o["taxa_count"]

            if label == 'NULL':
                continue

            if date not in seen:
                seen.append(date)
            if label not in labels:
                labels.append(label)
                temp[label] = {}

            temp[label][date] = count

        seen = sorted(seen)

        data = []
        data.append(seen)

        for key, val in temp.iteritems():
            row = [key]
            for s in seen:
                if s in val:
                    row.append(temp[key][s])
                else:
                    row.append(0)
            data.append(row)

        # label the x-axis for printing into c3
        seen.insert(0, 'x'.encode("utf-8"))
        data = sorted(data, key=lambda a_entry: a_entry[0])
        return data

    def getStackedBarChartData(self, filterHelper):
        ordersBySite = SubsampleModel.objects.select_related('sample__site').values(filterHelper.getSubSampleSubLocation(), filterHelper.getSubTaxa()).annotate(taxa_count=Count('species', distinct=True))
        ordersBySite = filterHelper.refineSubsampleQuery(ordersBySite)

        seen = []
        locations = []
        temp = {}
        for o in ordersBySite:

            label = o[filterHelper.getSubTaxa()].encode("utf-8")
            loc = o[filterHelper.getSubSampleSubLocation()].encode("utf-8")
            count = o["taxa_count"]

            if label == 'NULL':
                continue

            if label not in seen:
                seen.append(label)
                temp[label] = {}
            if loc not in locations:
                locations.append(loc)

            temp[label][loc] = count

        locations = sorted(locations)

        data = []
        data.append(locations)
        for key, val in temp.iteritems():
            count = 0
            row = [key]
            for loc in locations:

                if loc in temp[key]:
                    row.append(temp[key][loc])
                else:
                    row.append(0)

            data.append(row)

        # label the x-axis for printing into c3
        locations.insert(0, 'x'.encode("utf-8"))

        data = sorted(data, key=lambda a_entry: a_entry[0])
        return data

    def getTaxaTree(self):
        entries = SubsampleModel.objects.values('order_name', 'family', 'genus', 'species')

        taxa_tree = {}
        for entry in entries:
            order_name = _get_field(entry, 'order_name')
            if order_name != 'NULL':
                taxa_tree[order_name] = {}

        for entry in entries:
            family = _get_field(entry, 'family')
            if family != 'NULL':
                taxa_tree[_get_field(entry, 'order_name')][family] = {}

        for entry in entries:
            genus = _get_field(entry, 'genus')
            if genus != 'NULL':
                taxa_tree[_get_field(entry, 'order_name')][_get_field(entry, 'family')][genus] = {}

        for entry in entries:
            species = _get_field(entry, 'species')
            if species != 'NULL':
                taxa_tree[_get_field(entry, 'order_name')][_get_field(entry, 'family')][_get_field(entry, 'genus')][species] = True


        return taxa_tree

def _get_field(entry, field):
    return entry[field].encode('utf-8')
