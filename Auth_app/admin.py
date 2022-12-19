from django.contrib import admin
from.models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class UserModel(UserAdmin):
    list_display = ['username', 'User_type']
    

admin.site.register(CustomUser, UserModel)

admin.site.register(Course)
admin.site.register(Sessin_year)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)
admin.site.register(Student_Notification)
admin.site.register(Staff_leav)
admin.site.register(Staff_feedback)
admin.site.register(Student_feedback)
admin.site.register(Student_leav)
admin.site.register(Attendence)
admin.site.register(Attendence_report)
admin.site.register(Result)