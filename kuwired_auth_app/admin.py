from django.contrib import admin
from .models import CustomUser
class CustomUser_admin(admin.ModelAdmin):
    list_display=['username', 'email','first_name','last_name', 'phone_number', 'is_company', 'company_name', 'company_role','is_active']


admin.site.register(CustomUser,CustomUser_admin)

