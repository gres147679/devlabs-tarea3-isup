# Create your views here.
import models

from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def scan(request):
	if request.method == 'POST':
		website = models.WebSite(request.POST)
		website.siteAddress = request.POST['siteAddress']
		if website.is_valid():
			if website.exists():
				return render(request, 'isUp/up.html', {
					'websiteURL': "http://"+str(website.siteAddress)
				})
			else:
				#return HttpResponseRedirect('/isUp/bad/') # Redirect after POST
				return render(request, 'isUp/down.html', {
					'websiteURL': "http://"+str(website.siteAddress)
				})
	else:
		website = models.WebSite() # An unbound form

	template = loader.get_template('isUp/index.html')
	return render(request, 'isUp/index.html', {
        'website': website,
    })