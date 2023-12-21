from django.contrib import admin
from .models import Student
from .models import User
# Register your models here.
admin.site.register(User)
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['id','stuname','email']