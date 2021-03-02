from django.shortcuts import render,redirect
from app.models import Attendee,Meeting
from app.forms import AttendeeForm,MeetingForm,AttendeceForm
from django.views import View
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import  messages
def emailsend(request,pk):
    alist = Attendee.objects.all()
    desc = Meeting.objects.get(id=pk)
    for i in desc.attendee.all():
        template = render_to_string('email.html',{'name':i.name,'desc':desc})
        email = EmailMessage(
        'Thanks for purchasing the stuff from us',
        template,
        settings.EMAIL_HOST_USER,
        [i.email],
    )
        email.fail_silently=False
        email.send()
            
    return redirect("add")    
