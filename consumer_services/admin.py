from django.contrib import admin

from .models import ServiceRequest, UserProfile

# Register your models here.
admin.register(UserProfile)
admin.register(ServiceRequest)
