from django.shortcuts import render,redirect
from app.models import Attendee,Meeting
from app.forms import AttendeeForm,MeetingForm,AttendeceForm
from django.views import View
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import  messages

# code here
class AttendenceView(View):
    def get(self,request):
        fm =AttendeceForm()
        return render (request,'attendence.html',{'form':fm})
    def post(self,reqeust):
        fm = AttendeceForm(reqeust.POST)
        if fm.is_valid():
            fm.save()
        return redirect('add')
