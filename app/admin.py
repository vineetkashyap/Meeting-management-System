from django.contrib import admin
from. models import Meeting,Attendee,Attendence
# Register your models here.


@admin.register(Attendence)
class AttendenceAdmin(admin.ModelAdmin):
    list_dispaly = ['id','name','meet','status']

admin.site.register(Meeting)
admin.site.register(Attendee)
