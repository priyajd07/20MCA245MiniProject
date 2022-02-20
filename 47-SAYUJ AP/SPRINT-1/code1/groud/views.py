from django.shortcuts import render

# Create your views here.
from groud.models import Groud


def index(request):
    if request.method=="POST":
        obj=Groud()
        obj.lid=1
        obj.phone=request.POST.get('ph')
        obj.address=request.POST.get('adr')
        obj.email=request.POST.get('email')
        obj.gname=request.POST.get('nm')
        obj.logid=1
        obj.save()
    return render(request,"ground/ground.html")