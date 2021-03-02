from django import forms
from .models import Attendee,Meeting,Attendence

class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['name','email']
        widgets  ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})}

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets  ={
            'meeting_name':forms.TextInput(attrs={'class':'form-control'}),
            'meeting_link':forms.URLInput(attrs={'class':'form-control'}),'start_time':forms.TimeInput(attrs={'class':'form-control'}),'end_time':forms.TimeInput(attrs={'class':'form-control'}),'date':forms.DateInput(attrs={'class':'form-control'}),
            'discription':forms.Textarea(attrs={'class':'form-control'})
            }
class AttendeceForm(forms.ModelForm):
    class Meta:
        model = Attendence
        fields= '__all__'
        widgets  ={
            'meeting_name':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),}
