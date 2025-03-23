from django.shortcuts import render,redirect, HttpResponse
#from app.backend import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser, Officer, Member
#from django.http import JsonResponse
#from app.models import Sector, District, Teacher, Learning_Center, School_Year, ProgramCategory, ProgramType, Province, Municipality, Barangay

def HOME(request):
    return render(request,'homepage.html')

def LOGIN(request):
    return render(request,'login.html')

def ABOUT(request):
    return render(request,'about.html')

def ANNOUNCEMENT(request):
    return render(request,'announcement.html')

def REGISTRATION(request):
    return render(request,'registration.html')

def EVENTS(request):
    return render(request,'events.html')

def FORGOT_PASSWORD(request):
    return render(request,'forgot_password.html')

#feb282025
def doLogin(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)

        if user!=None:
            login(request, user)
            user_type = user.user_type
            print(f"User type: {user_type}") #Debugging line
            
            if user_type == '1':
               # messages.success(request, 'You have successfully logged in.')
                return redirect('hoo_home')
                # pass
            elif user_type == '2':
                #messages.success(request, 'You have successfully logged in.')
                return redirect('officer_home')
                # pass
            elif user_type == '3':
                #messages.success(request, 'You have successfully logged in.')
                return redirect('member_home')
                # pass
            else:
                #message
                messages.error(request, 'Email and Password are Invalid')
                return redirect('login')
        else:
        #message
            messages.error(request, 'Email  and Password are Invalid')
            return redirect('login')
            
def doLogout(request):
    logout(request)
    return redirect('homepage')

#testing users to display as list
#def officer_list(request):
    #return redirect('officer_list')
#@login_required(login_url='/')