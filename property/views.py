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
    crrProp.lang = 70
    crrProp.latt = -70
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


def listProperty(request, pid):
    pass


def search(request):
    query = request.GET.get('q')
    if query:
        props = Property.objects.filter(location__contains=query)
        if not props:
            props = Property.objects.all()
            return render(request, 'list-properties.html', {"props": props})
        else:
            return render(request, 'search_result.html', {'props': props})
    else:
        props = Property.objects.all()
        return render(request, 'list-properties.html', {"props": props})
