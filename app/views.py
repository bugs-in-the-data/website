from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from app.models import SubsampleModel
from app.models import SiteModel

# Create your views here.
def index(request):
	template = loader.get_template('index.html')

	subsample = SubsampleModel()
	site = SiteModel()
	print subsample.getTaxaTree()

	data = {
		'pie_chart' : subsample.getPieChartData(),
		'site_names' : site.getSiteNames(),
		'sites_tree' : site.getSitesTree(),
		'taxa_tree' : subsample.getTaxaTree(),
	}

	# test = subsample.getStackedBarChartData()

	return HttpResponse(template.render(data, request))
