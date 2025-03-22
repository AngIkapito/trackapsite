from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

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

class MemberType(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Specify the type for price
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class MembershipType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

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
    
class Announcement(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    banner = models.ImageField(upload_to='media/announcement')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_at = models.DateTimeField()  # Date and time when the announcement can be posted
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to the custom user model
    is_active = models.BooleanField(default=True)  # Indicates if the announcement is active

    def save(self, *args, **kwargs):
        # Automatically set is_active based on the current time and publish_at
        if self.publish_at < timezone.now():
            self.is_active = False
        else:
            self.is_active = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name