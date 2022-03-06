from django.shortcuts import render
from manager_registration.models import ManagerRegistration
from login.models import Login
from turf_location.models import TurfLocation
from django.http import HttpResponseRedirect

# Create your views here.
def mangr_reg(request):
    ob = TurfLocation.objects.all()
    context = {
        'objval':ob
    }
    if request.method =="POST":
        c=request.POST.get('tid')
        if ManagerRegistration.objects.filter(t_id=c).exists():
            msg="Turf Manager already exist"
            c={
                'ok':msg
            }
            return render(request, 'manager_reg/a_managerreg.html', c)
        else:
            turf = request.POST.get('tid')
            o = TurfLocation.objects.get(l_id=turf)


            obj = ManagerRegistration()
            obj.t_id = request.POST.get('tid')
            obj.name = request.POST.get("name")
            obj.address = request.POST.get("address")
            obj.phone = request.POST.get("phone")
            obj.district = request.POST.get("dist")
            obj.gender = request.POST.get("g")
            obj.dob = request.POST.get("dob")
            obj.email = request.POST.get("email")
            obj.turf_location = o.l_name
            obj.password = request.POST.get("pass")
            obj.repeatpassword = request.POST.get("repass")
            obj.save()

            ob = Login()
            ob.username = request.POST.get("email")
            ob.password = request.POST.get("pass")
            ob.u_id = obj.m_id
            ob.type = 'manager'
            ob.save()


    return render(request,'manager_reg/a_managerreg.html',context)


def edit_mangr(request,idd):
    obj = ManagerRegistration.objects.get(m_id=idd)
    conext = {
        'objva': obj
    }
    if request.method == 'POST':

        obj.name = request.POST.get("name")
        obj.phone = request.POST.get("phone")
        obj.dob = request.POST.get("dob")
        obj.gender =request.POST.get("g")
        obj.district = request.POST.get("dist")
        obj.address = request.POST.get("address")
        obj.email = request.POST.get("email")
        # obj.t_id = 9
        obj.save()
        return HttpResponseRedirect('/regmanager/managemanger/')
    return render(request,'manager_reg/a_editmanager.html',conext)


def manage_mangr(request):
    obj = ManagerRegistration.objects.all()
    conext = {
        'objva':obj
    }
    return render(request,'manager_reg/a_mange_manager.html',conext)


def delete(request,idd):
    print(idd)
    obj = ManagerRegistration.objects.get(m_id=idd)
    obj.delete()
    ob = Login.objects.get(u_id=idd,type='manager')
    ob.delete()
    return HttpResponseRedirect('/regmanager/managemanger/')
