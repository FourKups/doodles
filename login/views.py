from django.shortcuts import render
from rest_framework import viewsets
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import GUser,Post


@api_view(['GET', 'POST'])
def login(request):
    data = JSONParser().parse(request)
    if GUser.objects.filter(GmailId=data['gmailid']).exists():
        return Response({"status":True})
    else:
        new=GUser(FirstName=data['firstname'],LastName=data['lastname'],GmailId=data['gmailid'],DOB=data['dob'])
        new.save()
        return Response({"status": "success"})

@api_view(['GET', 'POST'])
def post(request):
    new=Post(GmailId=str(request.POST['gmailid']),File=request.FILES['file'],Caption=str(request.POST['caption']))
    new.save()
    return Response({"status":"success"})

@api_view(['GET', 'POST'])
def getpost(request):
    #data = JSONParser().parse(request)
    dbdata=Post.objects.all()
    dict={"array":[]}
    for i in dbdata:
        dict['array'].append({'postid':i.PostId,'gmailid':i.GmailId,"file":i.File.url,'likes':i.Likes,"caption":i.Caption})
    print(dict)
    return Response(dict)