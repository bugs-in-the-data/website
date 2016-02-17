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

	data = {
		'pie_chart' : subsample.getPieChartData(),
		'bar_chart' : subsample.getStackedBarChartData(),
	}

	test = subsample.getStackedBarChartData()

	return HttpResponse(template.render(data, request))
