from django.shortcuts import render,redirect, HttpResponse
#from app.backend import EmailBackEnd
# from django.contrib.auth import authenticate, logout, login
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from app.models import CustomUser, Officer, Member, School_Year
#from django.http import JsonResponse
#from app.models import Sector, District, Teacher, Learning_Center, School_Year, ProgramCategory, ProgramType, Province, Municipality, Barangay
 
# def HOME(request):
#     return render(request,'home.html')
    
def HOME(request):
    return render(request,'home.html')