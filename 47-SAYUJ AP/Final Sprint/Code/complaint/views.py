from django.shortcuts import render
from complaint.models import Complaint
from user.models import User
from django.http import HttpResponseRedirect
import datetime

# Create your views here.
def postcom(request):
    uid=request.session['uid']
    if request.method=="POST":

        obj=Complaint()
        ob= User.objects.get(u_id=uid)
        obj.name=ob.name
        obj.u_id=uid
        obj.phone=ob.phone
        obj.email=ob.email
        obj.address=ob.address
        obj.complaint=request.POST.get('c')
        obj.date=datetime.datetime.now()
        obj.reply="pending"
        obj.save()
    return render(request,'complaint/postcomplaint.html')

def ad_view_complaint(request):
    obj = Complaint.objects.all().order_by('-c_id')
    context ={
        'objva':obj
    }
    return render(request,'complaint/a_viewcomplaint.html',context)


def post_reply(request,idd):
    print(idd)
    if request.method=='POST':
        obj = Complaint.objects.get(c_id=idd)
        obj.reply = request.POST.get('se')
        obj.save()
        return HttpResponseRedirect('/complaint/viwcomp/')

    return render(request,'complaint/cmplntreplay.html')

def vrep(request):
    ss=request.session['uid']
    var=Complaint.objects.filter(u_id=ss)
    con={
        'obb':var
    }
    return render(request,'complaint/viewreply.html',con)

