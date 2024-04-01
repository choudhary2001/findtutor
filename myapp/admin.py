from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed in the admin interface for Student
    list_display = ('user', 'phone')

@admin.register(Teachers)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Teachers._meta.get_fields()]


class CustomAdminSite(admin.AdminSite):
    site_title = 'Tutor Finder'

# Register the custom admin site
admin_site = CustomAdminSite(name='custom_admin')