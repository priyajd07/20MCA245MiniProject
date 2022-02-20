from django.shortcuts import render

# Create your views here.
from .models import Login
def index(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pwd = request.POST.get("password")
        obj=Login.objects.filter(uname=uname,pwd=pwd)
        if len(obj)>0:
            ob=obj[0]
            return render(request, 'temp/admin_home1.html')

    return render(request,'login/index.html')