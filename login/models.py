from django.db import models


# Create your models here.
class GUser(models.Model):
    GmailId = models.EmailField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DOB = models.DateField()


class Post(models.Model):
    PostId = models.AutoField(primary_key=True)
    GmailId = models.EmailField()
    File=models.ImageField()
    Likes=models.IntegerField()
