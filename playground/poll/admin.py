from django.contrib import admin
from poll.models import Person
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display=('id','name','age','city','dob')

admin.site.register(Person,PersonAdmin)