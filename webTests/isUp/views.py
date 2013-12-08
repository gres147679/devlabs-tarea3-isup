# Create your views here.
import models

from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def good(request):
    return HttpResponse("The website is good")

def bad(request):
    return HttpResponse("The website is a shit")


def scan(request):
	if request.method == 'POST':
		website = models.WebSite(request.POST)
		website.siteAddress = request.POST['siteAddress']
		if website.is_valid():
			if website.exists():
				return HttpResponseRedirect('/isUp/good/') # Redirect after POST
			else:
				return HttpResponseRedirect('/isUp/bad/') # Redirect after POST
	else:
		website = models.WebSite() # An unbound form

	template = loader.get_template('isUp/index.html')
	return render(request, 'isUp/index.html', {
        'website': website,
    })