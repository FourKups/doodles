from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import GUser


@api_view(['GET', 'POST'])
def login(request):
    data = JSONParser().parse(request)
    if GUser.objects.filter(GmailId=data['gmailid']).exists():
        return Response({"status":True})
    else:
        new=GUser(FirstName=data['firstname'],LastName=data['lastname'],GmailId=data['gmailid'],DOB=data['dob'])
        new.save()
        return Response({"status": True})
