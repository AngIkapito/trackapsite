"""
URL configuration for trackapsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

from .import views, hoo_views, member_views, officer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', views.REGISTRATION, name='registration'),
    path('registration_bypass/', member_views.REGISTRATION_BYPASS, name='registration_bypass'),
    # path('registration_bypass1/', member_views.REGISTRATION_BYPASS1, name='registration_bypass1'),
    # path('registration_bypass2/', member_views.REGISTRATION_BYPASS2, name='registration_bypass2'),
    path('', views.HOME, name='home'),
    path('about/', views.ABOUT, name='about'),
    path('base/',views.BASE,name='base'),
    path('announcement/', views.ANNOUNCEMENT, name='announcement'),
    path('events/', views.EVENTS, name='events'),
    path('forgot_password/', views.FORGOT_PASSWORD, name='forgot_password'),

    #Login
    path('login',views.LOGIN,name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),
    
    #Profile Update
    path('profile', views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE, name='profile_update'),
    
    #President/Admin/Head of Organization Panel
    path('hoo/home', hoo_views.home, name='hoo_home'),
    
    # path('hoo/Member/Add', hoo_views.ADD_MEMBER, name='add_member'),
    # path('hoo/Member/View', hoo_views.VIEW_MEMBER, name='view_member'),
    # path('hoo/Member/Edit/<str:id>', hoo_views.EDIT_MEMBER, name='edit_member'),
    # path('hoo/Member/Update', hoo_views.UPDATE_MEMBER, name='update_member'),
    # path('hoo/Member/Delete/<str:id>', hoo_views.DELETE_MEMBER, name='delete_member'),
    
    path('hoo/SchoolYear/Add', hoo_views.ADD_SCHOOLYEAR, name='add_schoolyear'),
    path('hoo/SchoolYear/View', hoo_views.VIEW_SCHOOLYEAR, name='view_schoolyear'),
    path('hoo/SchoolYear/Edit/<str:id>', hoo_views.EDIT_SCHOOLYEAR, name='edit_schoolyear'),
    path('hoo/SchoolYear/Update', hoo_views.UPDATE_SCHOOLYEAR, name='update_schoolyear'),
    path('hoo/SchoolYear/Delete/<str:id>', hoo_views.DELETE_SCHOOLYEAR, name='delete_schoolyear'),
    #path('hoo/officer_list', hoo_views.officer_list, name='officer_list'),
    
    #Officer Panel
    path('officer/home', officer_views.home, name='officer_home'),
    
    #Member Panel
    path('member/home', member_views.home, name='member_home'),
    #path('member/registration_member', member_views.REGISTRATION_MEMBER, name='registration_member'),

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

