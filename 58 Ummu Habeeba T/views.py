from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from.models import*
from.forms import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here
def index(request):
    return render(request,'index.html')

def register(request):
    reg=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()

            reg=True
        else:
            HttpResponse("Invalid Form!!")
    else:
        user_form=UserForm()
        profile_form=ProfileForm()

    return render(request,'Register.html',{'register':reg,'user_form':user_form,'profile_form':profile_form})

def user_login(request):              
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('dashboard'))
            else:
                   return HttpResponse("Not active")
        else:
            return HttpResponse("Invalid username or password")
    else: 
        return render(request,'login.html')        


def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')