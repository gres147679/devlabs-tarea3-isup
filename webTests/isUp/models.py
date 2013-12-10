from django import forms
import httplib, socket

# Create your models here.


'''Model of a WebSite, which will be pinged for response'''
class WebSite(forms.Form):

	'''Address of the WebSite'''
	siteAddress = forms.CharField(max_length=120,required=True,label="")

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

	
	
