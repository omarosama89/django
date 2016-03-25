from django import forms

class PropertyForm(forms.Form):
	ptype = forms.CharField(label="Property type :",max_length=50)
	location = forms.CharField(label="Location :",max_length=50)
	lang = forms.IntegerField()
	latt = forms.IntegerField()
	price = forms.IntegerField(label="Price :")
	area = forms.IntegerField(label="Area :")
	img = forms.CharField(max_length=100)
	nrooms = forms.IntegerField(label="Number of rooms :")
	ntoilets = forms.IntegerField(label="Number of toilets :")