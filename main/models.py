from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from PIL import Image
from io import BytesIO
import time

from main.choices import *

# Create your models here.

class VendorProfile(models.Model):
  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(verbose_name="Company Name", max_length=100, null=True, blank=True)
    company_type = models.IntegerField(choices=COMPANY_CHOICES, default=4)
    image = models.ImageField(blank=True, null=True, upload_to='profile/')
    created_at = models.DateTimeField(auto_now_add=True)
 
    address = models.CharField(verbose_name="Address",max_length=100, null=True, blank=True)
    locality = models.CharField(verbose_name="City",max_length=100, null=True, blank=True)
    state = models.CharField(verbose_name="State",max_length=100, null=True, blank=True)
    postal_code = models.CharField(verbose_name="Zip Code",max_length=8, null=True, blank=True)
    country = models.CharField(verbose_name="Country",max_length=100, null=True, blank=True)


    def __str__(self):
	      return self.user.company_name
     
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs) 
 
    class Meta:
        ordering = ['-created_at']

class Brew(models.Model):

    name = models.CharField(max_length=100, null=True)
    brew_type = models.IntegerField(choices=BREW_CHOICES, default=1)
    brewery = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='brew/')
    
    def __str__(self):
        return self.name