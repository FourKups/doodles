from django.db import models
import datetime


# Create your models here.
class GUser(models.Model):
    GmailId = models.EmailField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DOB = models.DateField()


def update_filename(instance,filename):
    changedfilename = str(str(instance.GmailId).split('@')[0] + str(datetime.datetime.now()))
    return changedfilename

class Post(models.Model):
    PostId = models.AutoField(primary_key=True)
    GmailId = models.EmailField()
    File=models.ImageField(upload_to=update_filename)
    Likes=models.IntegerField(default=0)
    Caption=models.CharField(max_length=100,default="")

    def __str__(self):
         return str(self.PostId)
