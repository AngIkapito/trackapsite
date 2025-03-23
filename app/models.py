from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1, 'HOO'),
        (2, 'OFFICER'),
        (3, 'MEMBER'),
    )
    user_type = models.CharField(choices=USER, max_length=50,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    email = models.EmailField(max_length=150)
    middle_name = models.CharField(max_length=100,default="")
    contact_no = models.CharField(max_length=13,default="")

class Officer(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
        
class Member(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name

class School_Year(models.Model):
    sy_start = models.DateField()
    sy_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.sy_start.year}-{self.sy_end.year}"

class Region(models.Model):
    region_name = models.CharField(max_length=100)
    region_description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.region_name
    
class Organization(models.Model):
    initials = models.CharField(max_length=10)
    org_name = models.CharField(max_length=200)
    org_logo = models.ImageField(upload_to='media/org_logo')
    
    def __str__(self):
        return self.org_name