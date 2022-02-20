from django.shortcuts import render

# Create your views here.
from location.models import Location


def index(request):
    if request.method=="POST":
        loc=request.POST.get('loc')
        ob=Location()
        ob.location=loc
        ob.save()

    return render(request,"location/addlocation.html")