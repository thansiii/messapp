from abc import abstractmethod
from django.db import models 
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_mess = models.BooleanField(default=False, verbose_name='Is Mess')
    is_customer = models.BooleanField(default=False, verbose_name='Is Customer')
    name = models.CharField(max_length=100, default='User')
    mobile_number = models.CharField(max_length=20, default='Nil')
    bank_name = models.CharField(max_length=100, default='Nil')
    bank_account_number = models.CharField(max_length=50, default='Nil')
    ifcs_code = models.CharField(max_length=20, default='Nil')
    upi_id = models.CharField(max_length=100, default='Nil')
    # profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    location = models.CharField(max_length=300, default='Nil')
    address = models.TextField(max_length=1000, default='Nil')
    district = models.CharField(max_length=50, default='Nil')


    def __str__(self):
        return self.username                              
    