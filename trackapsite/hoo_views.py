from django.shortcuts import render,redirect, HttpResponse
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import CustomUser
#from django.http import JsonResponse

@login_required(login_url='/')
def home(request):
    return render(request,'hoo/home.html')

def ADD_OFFICER(request):
    return render(request,'hoo/add_officer.html')

def ADD_MEMBER(request):
    return render(request,'hoo/add_member.html')

def VIEW_MEMBER(request):
    return render(request,'hoo/view_member.html')

# def OFFICER_LIST(request):
#     return render(request,'hoo/officer_list.html')

# def VIEW_OFFICER(request):
#     id = request.GET.get('CustomUser')
    
#     #users = CustomUser.objects.filter(id__province_name='Pampanga')
    
#     if id:
#         user = CustomUser.objects.filter(id=id)
#     else:    
#         user = CustomUser.objects.all()
    
#     context = {
#         'user':user,
#         #'municipalities':municipalities
#     }
#     print(user)
#     return render(request, 'hoo/VIEW_OFFICER.html', context)

# @login_required(login_url='/')
# def ADD_OFFICER(request):
#     #region = Region.objects.all()
    
#     if request.method == "POST":
#         #profile_pic = request.FILES.get('profile_pic')
#         first_name = request.POST.get('first_name').upper()
#         last_name = request.POST.get('last_name').upper()
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         #gender = request.POST.get('gender')
#         #mobile = request.POST.get('mobile')
        
#         if  CustomUser.objects.filter(email=email).exists():
#              messages.warning(request,'Email is already taken')
#              return redirect('add_student')
#         if  CustomUser.objects.filter(username=username).exists():
#              messages.warning(request,'Username is already taken')
#              return redirect('add_student')     
#         else:
#             user = CustomUser(
#                 first_name = first_name,
#                 last_name = last_name,
#                 username = username,
#                 email = email,
#                 #profile_pic = profile_pic,  
#                 user_type = 2,
#             )        
#             user.set_password(password)
#             user.save()
            
#             officer = Officer (
#                 admin = user,
#                 #gender = gender,
#                 #mobile = mobile,
                
                
#             )
#             officer.save()
#             messages.success(request,user.first_name + " " + user.last_name + " is successfully added")
#             return redirect('add_officer')
        
#     context = {
#         'region':region,
#     }
#     return render(request,'hoo/add_officer.html',context)

