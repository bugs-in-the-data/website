from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app.models import SubsampleModel

# Create your views here.
def index(request):
	template = loader.get_template('index.html')

	species = SubsampleModel()
	test = species.getData()

	return HttpResponse(template.render(test, request))
