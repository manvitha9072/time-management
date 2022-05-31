from pickle import FALSE
from django.db import models
class Home(models.Model):
    name=models.CharField(max_length=122, default='name')
    phnumber=models.CharField(max_length=122, default='91')
    mailid=models.CharField(max_length=122, default='xyz@mail.com')
    prof=models.CharField(max_length=122, default='asdd')
    age=models.CharField(max_length=122, default='122')

class Newschedule(models.Model):
    name=models.CharField(max_length=60, null=True)
    time=models.IntegerField(null=True)
    title=models.CharField(max_length=50, null=True)
    desc=models.CharField(max_length=300, null=True)
    
#git experiment
#hello

