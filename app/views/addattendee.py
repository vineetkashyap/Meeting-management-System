from django.shortcuts import render,redirect
from app.models import Attendee,Meeting
from app.forms import AttendeeForm,MeetingForm,AttendeceForm
from django.views import View
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import  messages
class AddAttendee(View):
    def get(self,request):
        form = AttendeeForm()
        form2 = Meeting.objects.all()
        return render(request,'attendee.html',{'form':form,'form2':form2})
    def post(self,request):
        fm = AttendeeForm(request.POST)
        if fm.is_valid():
            fm.save()
        form = AttendeeForm()
        form2 = Meeting.objects.all()
        return render(request,'attendee.html',{'form':form,'form2':form2})