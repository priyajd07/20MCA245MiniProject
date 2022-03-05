from django.shortcuts import render
from login.models import Login
# Create your views here.


def login(request):
    if request.method == "POST":
        unm = request.POST.get('username')
        pwd = request.POST.get('pass')

        print(unm)
        print(pwd)

        obj = Login.objects.filter(username=unm,password=pwd)
        for x in obj:
            ty = x.type
            u_id = x.u_id

            if ty == 'admin':
                request.session['uid'] = u_id
                return render(request,'temp/ad_home.html')
            elif ty == 'manager':
                request.session['uid'] = u_id
                return render(request, 'temp/manager_home.html')
            elif ty == 'user':
                request.session['uid'] = u_id
                return render(request, 'temp/aidteam_home.html')
        msg="Incorrect username or password!!"
        context={
            'ok':msg
        }
        return render(request, 'login/login.html',context)
    return render(request,'login/login.html')



