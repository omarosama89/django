from django.shortcuts import render
from forms import PropertyForm
from models import Property
from django.http import HttpResponse
# Create your views here.




def addProperty(request):
	form = PropertyForm()
	return render(request, 'add-property.html',{'form':form.as_p()})

def editProperty(request,pid):
	form = PropertyForm()
	try:
		crrProp = Property.objects.get(pk = pid)
	except Property.DoesNotExist:
		return HttpResponse()
	return render(request, 'edit-property.html',{'form':form.as_p(),'ptype':crrProp.ptype,'location':crrProp.location,'price':crrProp.price,'area':crrProp.area,'img':crrProp.img,'nrooms':crrProp.nrooms,'ntoilets':crrProp.ntoilets,'owner':crrProp.owner.id})

def updateProperty(request):
	form = PropertyForm()
	try:
		if 'owner' not in request.POST:
			crrProp = Property()
		else:
			pid = request.POST.get('owner','')
			crrProp = Property.objects.get(pk = pid)
	except Property.DoesNotExist:
		return HttpResponse("no prtoperty with this id")
	crrProp.ptype = request.POST['ptype']
	crrProp.location = request.POST['location']
	crrProp.price = request.POST['price']
	crrProp.area = request.POST['area']
	crrProp.nrooms = request.POST['nrooms']
	crrProp.ntoilets = request.POST['ntoilets']
	crrProp.save()

	return render(request, 'add-property.html',{'form':form.as_p()})	