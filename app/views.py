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

	data = {
		'pie_chart' : subsample.getPieChartData(),
        'samples'   : sample.getAllSamples(),
	}

	test = subsample.getStackedBarChartData()

	return HttpResponse(template.render(data, request))
