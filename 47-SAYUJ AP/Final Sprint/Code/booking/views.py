from django.shortcuts import render
from booking.models import Booking
# from django.db import connection
from user.models import User
from django.http import HttpResponseRedirect
import datetime
from turf_location.models import TurfLocation
from time_slot.models import TimeSlot

# Create your views here.

def booking(request):
    mid = request.session['uid']
    obj = Booking.objects.filter(status='pending',m_id=mid)
    context ={
        'objva':obj
    }
    return render(request,'booking/m_viewbooking.html',context)


def tdybooking(request):
    lg=datetime.date.today()
    mid = request.session['uid']
    obj = Booking.objects.filter(date=lg,status='approved',m_id=mid)
    cdt ={
        'objv':obj
    }
    return render(request,'booking/m_tdy_bookig.html',cdt)


def delete(request,idd):
    print(idd)
    obj = Booking.objects.get(b_id=idd)
    obj.delete()
    return HttpResponseRedirect('/booking/book/')


def bapprove(request,idd):
    obj = Booking.objects.get(b_id=idd)
    ob = TimeSlot.objects.filter(t_id=obj.t_id)
    cntext = {
        'ob':ob,
        'obj':obj,
    }
    if request.method == "POST":
        a = request.POST.get('s')
        obj.status='approved with #'+str(a)
        obj.save()
        return booking(request)
    return render(request, 'booking/book2.html',cntext)

def bookstatuss(request):
    ss=request.session['uid']
    obj=Booking.objects.filter(u_id=ss)
    context={
        'objval':obj,
    }
    return render(request,'booking/viewbookingstatus.html',context)
from manager_registration.models import ManagerRegistration
from django.http import HttpResponseRedirect
def book(request,idd):
    if request.method=="POST":
        ss=request.session['uid']
        user=User.objects.get(u_id=ss)
        print(idd)
        print(ss)
        turf=TurfLocation.objects.get(l_id=idd)
        mn=ManagerRegistration.objects.get(t_id=idd)
        print(mn.m_id)

        obj=Booking()
        obj.u_id=ss
        obj.m_id=mn.m_id
        obj.t_id=idd
        obj.turflocation=turf.l_name
        obj.name=user.name
        obj.phone=user.phone
        obj.email=user.email
        obj.date=request.POST.get('da')
        obj.time=request.POST.get('time')
        obj.status="pending"

        obj.save()
        msg = "turf Booked"

        c = {
            'kp': msg
        }

        return render(request,'booking/bookkkkkuser.html',c)
    return render(request,'booking/bookkkkkuser.html')
