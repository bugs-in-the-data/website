from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from app.models import SubsampleModel
from app.models import SiteModel
from app.models import SampleModel
from app.helpers import FilterHelperModel

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# Create your views here.
def index(request):
    template = loader.get_template('index.html')

    filterHelper = FilterHelperModel()
    subsample = SubsampleModel()
    site = SiteModel()
    sample = SampleModel()

    filter_object = filterHelper.getFilterObject()

    if request.POST:
        filter_object = filterHelper.handleFilterPostData(request.POST)
        # print filter_object

    data = {
        'site_names' : site.getSiteNames(),
        'sites_tree' : sample.getSitesTree(),
        'taxa_tree' : subsample.getTaxaTree(),
        'pie_chart'  : subsample.getPieChartData(),
        'bar_chart'  : subsample.getStackedBarChartData(),
        'line_chart' : subsample.getLineChartData(),
        'samples'   : sample.getAllSamples(),
        'filter_object' : filter_object,
        'lowest_levels' : filterHelper.getLowestLevels(),
    }

    # test = subsample.getStackedBarChartData()

    return HttpResponse(template.render(data, request))
