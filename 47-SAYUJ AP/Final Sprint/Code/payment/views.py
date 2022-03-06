from django.shortcuts import render
from payment.models import Payment
from manager_registration.models import ManagerRegistration
from user.models import User
import datetime


# Create your views here.
def payment(request):
    obj = Payment.objects.all()
    context = {
        'objva':obj
    }
    return render(request,'payement/m_viewpayment.html',context)
def addpayment(request,idd,idi):
    if request.method == "POST":
        ss = request.session['uid']
        user = User.objects.get(u_id=ss)
        # mn = ManagerRegistration.objects.get(m_id=idi)
        obj=Payment()
        obj.email=user.email
        obj.u_id=ss
        obj.date=datetime.datetime.now()
        obj.phone=user.phone
        obj.name=user.name
        obj.m_id=idi
        obj.b_id=idd
        obj.amount=request.POST.get('p')
        obj.save()
        msg = "Paid Succesfully"
        context={
            'ok':msg
        }
        return render(request, 'payement/pay.html',context)
    return render(request,'payement/pay.html')


# from django.http import HttpResponse
# from rest_framework.views import APIView,Response
# # from payment.serializer import android_serializer
# from user.models import User
# from booking.models import Booking
# class pay_view(APIView):
#     def get(self,request):
#         ob=Payment.objects.all()
#         ser=android_serializer(ob,many=True)
#         return Response(ser.data)
#     def post(self,request):
#         uid = request.data['u_id']
#         obj = User.objects.get(u_id=uid)
#
#
#         ob = Payment()
#         ob.b_id = request.data['b_id']
#         ob.u_id=request.data['u_id']
#         ob.m_id=request.data['m_id']
#         ob.name=obj.name
#         ob.phone=obj.phone
#         ob.email = obj.email
#         ob.amount = request.data['amount']
#         ob.date = datetime.date.today()
#         ob.save()
#
#         o = Booking.objects.get(id=request.data['b_id'])
#         o.status = 'paid'
#         o.save()
#
#         return HttpResponse('POST')
