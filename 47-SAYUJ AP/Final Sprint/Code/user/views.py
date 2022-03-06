from django.shortcuts import render

from login.models import Login
from user.models import User


# Create your views here.

def usrreg(request):
    if request.method=="POST":


        obj = User()

        obj.name = request.POST.get("name")
        obj.address = request.POST.get("address")
        obj.phone = request.POST.get("phone")
        # obj.district = request.POST.get("dist")
        # obj.gender = request.POST.get("g")
        obj.place = request.POST.get("address")
        obj.email = request.POST.get("em")
        # obj.turf_location = .l_name
        obj.password = request.POST.get("pass")
        obj.repeatpassword = request.POST.get("repass")
        obj.save()

        ob = Login()
        ob.username = request.POST.get("em")
        ob.password = request.POST.get("pass")
        ob.u_id= obj.u_id
        ob.type = 'user'
        ob.save()


    return render(request,'user/user.html')


