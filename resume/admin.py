from django.contrib import admin
from .models import Resume 

class ResumeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Contacts', {'fields':['full_name','email','phone','address']}),
        ('Education',{'fields':['school','degree']}),
        ('Skils and Accomplishments (comma seperated)',{'fields':['skills','accomplishments']})
    ]

admin.site.register(Resume,ResumeAdmin)
