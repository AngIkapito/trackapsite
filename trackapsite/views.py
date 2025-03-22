from django.shortcuts import render,redirect, HttpResponse
#from app.backend import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser, Officer, Member, School_Year
#from django.http import JsonResponse
#from app.models import Sector, District, Teacher, Learning_Center, School_Year, ProgramCategory, ProgramType, Province, Municipality, Barangay

def BASE(request):
    return render(request,'base.html')
    
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

@login_required(login_url='/')  
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    
    context = {
        "user":user,
    }
    return render(request, 'profile.html', context)

@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(profile_pic, first_name, last_name, email, username, password)
        
        try:
            customuser = CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name
            
            if password !=None and password != "":
                customuser.set_password(password)
            
            if profile_pic !=None and profile_pic != "":
                customuser.profile_pic = profile_pic

            customuser.save()
            messages.success(request,'Your Profile updated successfully!')
            return redirect('profile')
        except:
            messages.error(request, 'Failed to update your profile')
    return render(request,'profile.html')    

