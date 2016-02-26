from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from app.models import SubsampleModel
from app.models import SiteModel
from app.models import SampleModel

# Create your views here.
def index(request):
	template = loader.get_template('index.html')

	subsample = SubsampleModel()
	site = SiteModel()
	sample = SampleModel()

	# data_filter = handleDataFilter(post)

	data = {
		'site_names' : site.getSiteNames(),
		'sites_tree' : site.getSitesTree(),
		'taxa_tree' : subsample.getTaxaTree(),
		'pie_chart'  : subsample.getPieChartData(),
		'bar_chart'  : subsample.getStackedBarChartData(),
		'line_chart' : subsample.getLineChartData(),
        'samples'   : sample.getAllSamples(),
	}

	# test = subsample.getStackedBarChartData()

	return HttpResponse(template.render(data, request))
