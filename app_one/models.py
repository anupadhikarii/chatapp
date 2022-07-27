from django.db import models
from django.forms import CharField
# Create your models here.
from django.contrib.auth.models import User


class Rooms(models.Model):

     admin =  models.CharField(max_length=150)
     room = models.CharField(max_length=250)
     password = models.CharField(max_length=500)

     def __str__(self) -> str:
        return self.room

class global_message(models.Model):

   message = models.CharField(max_length=500)
   message_send_by = models.CharField(max_length=50)
   date = models.DateField(auto_now_add=True)

   def __str__(self):
       return self.message_send_by
   
class Room_message(models.Model):
   
   room = models.ForeignKey( Rooms,on_delete=models.CASCADE)
   room_message = models.CharField(max_length=5000 )
   message_send_by = models.CharField(max_length=50, default=None)

   date = models.DateField(auto_now_add=True) 