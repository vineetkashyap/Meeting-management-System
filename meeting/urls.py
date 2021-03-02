
from django.contrib import admin
from django.urls import path
from  app.views.addmeet import AddMeet
from  app.views.addattendee import AddAttendee
from  app.views.attendence import AttendenceView
from app.views.emailsend import emailsend
urlpatterns = [
    path('admin/', admin.site.urls),
    path('send/<int:pk>',emailsend,name='send'),
    path('meet/', AddMeet.as_view(),name='meet'),
    path('att/',AttendenceView.as_view(),name='att'),
    path('',AddAttendee.as_view(),name='add'),
]
