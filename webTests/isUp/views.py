# Create your views here.
import models

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def scan(request):
	if request.method == 'POST':
		website = models.WebSite(request.POST)
		if website.is_valid():
			return HttpResponseRedirect('/thanks/') # Redirect after POST
	else:
		website = models.WebSite() # An unbound form

	template = loader.get_template('isUp/index.html')
	return render(request, 'index.html', {
        'website': website,
    })