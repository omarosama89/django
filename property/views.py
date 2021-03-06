from django.shortcuts import render
from forms import PropertyForm
from userlogin.models import Client
from models import Property
from django.http import HttpResponse
from os import path
from django import forms


# from forms import ModelFormWithFileField
# Create your views here.




def addProperty(request):
    form = PropertyForm()
    return render(request, 'add-property.html', {'form': form.as_p()})


def insertProperty(request):
    pass


def editProperty(request, pid):
    form = PropertyForm()
    try:
        crrProp = Property.objects.get(pk=pid)
    except Property.DoesNotExist:
        return HttpResponse()
    return render(request, 'edit-property.html',
                  {'form': form.as_p(), 'ptype': crrProp.ptype, 'location': crrProp.location, 'price': crrProp.price,
                   'area': crrProp.area, 'img': crrProp.img, 'nrooms': crrProp.nrooms, 'ntoilets': crrProp.ntoilets,
                   'owner': crrProp.owner.id})


def handle_uploaded_file(f, fpath):
    with open(fpath, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def updateProperty(request):
    form = PropertyForm()
    try:
        if 'owner' not in request.POST:
            crrProp = Property()
        else:
            pid = request.POST.get('owner', '')
            crrProp = Property.objects.get(pk=pid)
    except Property.DoesNotExist:
        return HttpResponse("no prtoperty with this id")
    crrProp.ptype = request.POST['ptype']
    crrProp.location = request.POST['location']
    crrProp.price = request.POST['price']
    crrProp.area = request.POST['area']
    crrProp.nrooms = request.POST['nrooms']
    crrProp.ntoilets = request.POST['ntoilets']
    crrProp.lang = request.POST['long']
    crrProp.latt = request.POST['lat']
    # crrProp.lang = 70
    # crrProp.latt = 40
    SITE_ROOT = path.dirname(path.dirname(path.realpath(__file__)))
    user = Client.objects.get(pk=1)
    crrProp.owner = user
    crrProp.save()

    fname = request.FILES['fileToUpload'].name
    extension = fname.split(".")[-1]

    imgName = str(crrProp.id) + "." + extension
    imgPath = SITE_ROOT + "/aqarmap/static/img/" + imgName
    handle_uploaded_file(request.FILES['fileToUpload'], imgPath)
    # form = ModelFormWithFileField(request.POST, request.FILES)
    # if form.is_valid():
    # 	form.save()
    crrProp.img = imgName
    crrProp.save()

    return render(request, 'add-property.html', {'form': form.as_p()})


def listProperties(request):
    props = Property.objects.all()
    return render(request, 'list-properties.html', {"props": props})


def listPropertiesCRUD(request):
    user = Client.objects.get(pk=1)
    props = Property.objects.filter(owner=user)
    return render(request, 'list-properties-crud.html', {"props": props})


def listProperty(request, pid):
    prop = Property.objects.get(pk=pid)
    return render(request, 'list-property.html', {"prop": prop})


def deleteProperty(request, pid):
    prop = Property.objects.get(pk=pid)
    prop.delete()
    user = Client.objects.get(pk=1)
    props = Property.objects.filter(owner=user)
    return render(request, 'list-properties-crud.html', {"props": props})
# if appartType and government and saleOrRent and minPrice and maxPrice and location:
#     props = Property.objects.filter(location__contains=location, ptype__contains=appartType,
#                                     price__range=[minPrice, maxPrice], saleOrRent__contains=saleOrRent,
#                                     government__contains=government)

def search(request):
    # query = request.GET.get('q')
    location = request.GET.get('location')
    government = request.GET.get('government')
    saleOrRent = request.GET.get('saleOrRent')
    minPrice = request.GET.get('minPrice')
    maxPrice = request.GET.get('maxPrice')
    appartType = request.GET.get('appartType')
    if appartType and government and saleOrRent and minPrice and maxPrice and location:
        props = Property.objects.filter(location__contains=location, ptype__contains=appartType,
                                        price__range=[minPrice, maxPrice], saleOrRent__contains=saleOrRent,
                                        government__contains=government)
        if not props:
            props = Property.objects.all()
            return render(request, 'list-properties.html', {"props": props, "no": "No Result"})
        else:
            allResult = Property.objects.all()
            return render(request, 'search_result.html', {'props': props, 'allResult': allResult})
    else:
        props = Property.objects.all()
        return render(request, 'list-properties.html', {"props": props})
