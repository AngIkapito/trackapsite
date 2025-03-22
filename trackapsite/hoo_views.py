from django.shortcuts import render,redirect, HttpResponse
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import CustomUser, School_Year
from django.db.models import Q  # Import Q
from django.template.loader import render_to_string
from django.http import JsonResponse
#from django.http import JsonResponse

@login_required(login_url='/')
def home(request):
    return render(request,'hoo/home.html')

# For Schoolyear 
def ADD_SCHOOLYEAR(request):
    if request.method == "POST":
        sy_start = request.POST.get('sy_start')
        sy_end = request.POST.get('sy_end')
        # print(program_name)
        school_year = School_Year (
            sy_start = sy_start,
            sy_end = sy_end,
        )
        school_year.save()
        messages.success(request, 'Cycle successfully added!')
        return redirect('add_schoolyear')
    return render(request, 'hoo/add_schoolyear.html')

def VIEW_SCHOOLYEAR(request):
    schoolyear = School_Year.objects.all()
    
    context = {
        'schoolyear':schoolyear,
    }
    # print(teacher)
    return render(request, 'hoo/view_schoolyear.html', context)


def EDIT_SCHOOLYEAR(request, id):
    schoolyear = School_Year.objects.filter(id = id)
    
    context = {
        'schoolyear':schoolyear
    }
    
    return render(request,'hoo/edit_schoolyear.html', context)


def UPDATE_SCHOOLYEAR(request):
    if request.method == "POST":
        id = request.POST.get('id')
        sy_start = request.POST.get('sy_start')
        sy_end = request.POST.get('sy_end')
        # print(program)
        
        schoolyear = School_Year.objects.get(id = id)
        schoolyear.sy_start = sy_start
        schoolyear.sy_end = sy_end
        
        schoolyear.save()
        
        messages.success(request, "Cycle successfully updated")
        return redirect('view_schoolyear')
    return render(request, 'hoo/edit_schoolyear.html')

def DELETE_SCHOOLYEAR(request, id):
    schoolyear = School_Year.objects.get(id = id)
    schoolyear.delete()
    messages.success(request, 'Cycle successfully deleted')
    return redirect('view_schoolyear')

# For Member