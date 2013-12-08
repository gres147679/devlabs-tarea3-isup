from django import forms
from django.core.validators import URLValidator
import httplib, socket

# Create your models here.


'''Model of a WebSite, which will be pinged for response'''
class WebSite(forms.Form):

	'''Address of the WebSite'''
	siteAddress = forms.URLField(required=True,label="Site address",validators=[URLValidator])

	def is_valid(self):
		return True


	def exists(self):
		try:
			conn = httplib.HTTPConnection(str(self.siteAddress))
			conn.request('HEAD', '')
			response = conn.getresponse()
			conn.close()
			return response.status < 500
		except socket.gaierror,e:
			return False

	
	
