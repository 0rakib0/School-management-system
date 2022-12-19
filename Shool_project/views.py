import email
from django.http import HttpResponse
from unicodedata import name
from django.shortcuts import render, redirect
from Auth_app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Auth_app.models import CustomUser


def index(request):
    diction = {}

    return render(request, 'base.html', context=diction)



def loadin_page(request):
    diction = {}
    return render(request, 'login.html', context=diction)


def do_login(request):
    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = EmailBackEnd.authenticate(request, username=email, password=password)
        if user !=None:
            login(request, user)
            user_type = user.User_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('staff_home')

            elif user_type == '3':
                return redirect('stu_home')
            else:
                messages.error(request, 'email and password not same! please try again')
                return redirect('login')

        else:
            messages.error(request, 'email and password notsame! please try again')
            return redirect('login')

def doLogout(request):
    logout(request)
    return redirect('login')
@login_required
def profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    diction = {
        'user':user
    }
    return render(request, 'Hod/profile.html', context=diction)

@login_required
def Profile_update(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            customeuser = CustomUser.objects.get(id = request.user.id)
            customeuser.first_name = first_name
            customeuser.last_last = last_name
            if profile_pic !=None and profile_pic != '':
                customeuser.profile_pic = profile_pic

            if password !=None and password != '':
                customeuser.set_password(password)
            customeuser.save()
            messages.success(request, 'Your Profile Updated Successfully')
            return redirect('profile')
        except:
            messages.error(request, 'Your profile update faild!')
    diction = {}
    return render(request, 'Hod/profile.html', context=diction)