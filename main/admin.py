from django.contrib import admin
from .models import VendorProfile, Brew

# Register your models here.

admin.site.register(VendorProfile)
admin.site.register(Brew)