from django.shortcuts import render
from feedback.models import Feedback
from django.http import HttpResponseRedirect
import datetime
# Create your views here.

def feedback(request):
    obj = Feedback.objects.all().order_by('-f_id')
    context = {
        'objva':obj
    }

    return render(request,'feedback/a_viewfeedback.html',context)

def feedbackreplay(request,idd):
    print(idd)
    if request.method == 'POST':
        obj = Feedback.objects.get(f_id=idd)
        obj.reply = request.POST.get('re')
        obj.save()

        return HttpResponseRedirect('/feedback/viewfeed/')

    return render(request,'feedback/a_feedbackreplay.html')

def feedbackp(request):
    ss=request.session['uid']
    if request.method=="POST":
        obj=Feedback()
        obj.feedback=request.POST.get('f')
        obj.date=datetime.datetime.now()
        obj.reply="pending"
        obj.u_id=ss
        obj.save()
    return render(request,'feedback/feedback.html')

