

from django.contrib import admin
from .models import Profile_Model, JobCity

@admin.register(JobCity)
class JobCityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Profile_Model)
class Profile_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'city', 'pin', 'state', 'mobile', 'email', 'password']
    list_display_links = ['id', 'name'] 
    search_fields = ['name', 'city', 'state']
    filter_horizontal = ('job_city',)  # Enables dual-list selection