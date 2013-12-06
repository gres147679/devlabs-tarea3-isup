from django import forms

# Create your models here.


'''Model of a WebSite, which will be pinged for response'''
class WebSite(forms.Form):

	'''Address of the WebSite'''
	siteAddress = forms.CharField(max_length=40,required=True,label="Site address")

	def is_valid(self):
		return True
	
	
