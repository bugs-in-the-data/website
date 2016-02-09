from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from app.models import SubsampleModel

# Create your views here.
def index(request):
	template = loader.get_template('index.html')

	subsample = SubsampleModel()

	data = {
		'bar_chart' : subsample.getData(),
	}

	return HttpResponse(template.render(data, request))
