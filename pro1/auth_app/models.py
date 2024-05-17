from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER = [('male', 'male'), ('female','female'),('other','other')]
    ROLES= [('manager','manager'),('team leader','team leader'),('developer','developer')]

    gender = models.CharField(max_length=6, choices=GENDER, default="male")
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True,null=True)
    city = models.CharField(max_length=30, blank=True,null=True)
    role = models.CharField(max_length=30, choices=ROLES, default='manager')
    company = models.CharField(max_length=30, blank=True,null=True)
    contact = models.BigIntegerField(blank=True, null=True)
