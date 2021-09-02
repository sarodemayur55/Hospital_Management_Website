from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.utils.html import escape, mark_safe

# Create your models here.



# class User(AbstractUser):
#     is_patient = models.BooleanField(default=False)
#     is_doctor = models.BooleanField(default=False)

class name(models.Model):
    n= models.CharField(max_length=100)

class contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    description = models.TextField()

class patient_appointment(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(blank=True)
    gend=[
        ("male","male"),
        ("female" , "female")
    ]
    gender = models.CharField(max_length=10, choices=gend)
    description = models.TextField()
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    username=models.CharField(max_length=50, default="", editable=False)
    doctorname=models.CharField(max_length=50,default="", editable=False)
    doctorusername=models.CharField( max_length=50,default="")


# class doctorlogin(models.Model):
#     username = models.CharField(max_length=20)e
#     password = models.CharField(max_length=20)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    



class specialist(models.Model):
    sid = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=50)


class doctordata(models.Model):
    itemid = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=50)
    sid = models.IntegerField()
    username=models.CharField(max_length=50,default="")

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

