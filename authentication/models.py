from django.db import models

# Create your models here.

class Coders(models.Model):
    name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    otp = models.IntegerField()
    otp_exp = models.DateTimeField(auto_now=True)
    role = models.IntegerField()
    profile_img = models.CharField(max_length=255)
    notification = models.BooleanField(default=True)


    
