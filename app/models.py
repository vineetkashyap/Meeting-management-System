from django.db import models

# Create your models here.
class Attendee(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    attedence  =models.BooleanField(blank=True,null=True,default=None)
    def __str__(self):
        return self.name
    
    
class Meeting(models.Model):
    meeting_name =models.CharField( max_length=50) 
    meeting_link = models.URLField( max_length=200)
    attendee=models.ManyToManyField(Attendee)
    start_time= models.TimeField(default='12:00:00')
    end_time= models.TimeField(default='12:00:00')
    date = models.DateField(auto_now=False, auto_now_add=False)
    discription = models.TextField(max_length=500)
    def attendees(self):
        return ",".join([str(p) for p in self.attendee.all()])
    def __str__(self):
        return self.meeting_name
ATTENDENCE = [
    ('Present','Present'),
    ('Absent','Absent'),
]
class Attendence(models.Model):
    meet = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    name  = models.CharField(max_length=50)
    status = models.CharField(choices=ATTENDENCE, max_length=50,default='None')
    def __str__(self):
        return self.name
    
