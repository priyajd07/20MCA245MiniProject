from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from room.models import Room
from chat.models import Chat
import datetime
from room_members.models import RoomMembers
# Create your views here.



def select_room(request):
    uid = request.session["uid"]
    room = RoomMembers.objects.filter(member_id=uid)
    # print(room)
    context = {
        'details': room,
    }
    return render(request,'chat/select_room.html',context)


def chats(request,idd):
    uid = request.session["uid"]
    obb=Chat.objects.filter(rm_id=idd)
    print(obb)
    context={
        'chats':obb.order_by('-time')
    }
    if request.method=="POST":
        obj=Chat()
        obj.user_id=uid
        obj.chat=request.POST.get('chat')

        fs = FileSystemStorage()
        videopath = request.FILES.get('media', False)
        # print(photopath)
        # print(videopath)
        if videopath != False:
            print("EEEEEEEE")
            vdo = request.FILES['media']
            vdoname = fs.save(vdo.name, vdo)
            obj.media = vdo.name
        else:
            obj.media = ""

        obj.date=datetime.date.today()
        obj.time=datetime.datetime.now().strftime("%I:%M:%S")
        obj.rm_id=idd
        obj.save()

    return render(request,'chat/chat.html',context)