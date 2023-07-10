from django.shortcuts import render
from . models import Place,Team

# Create your views here.

def demo(req):
    obj = Place.objects.all()
    obj2 = Team.objects.all()
    return render(req, "index.html",{'result': obj, 'Person': obj2})

def contact(req):
    return render(req, "contact.html")

