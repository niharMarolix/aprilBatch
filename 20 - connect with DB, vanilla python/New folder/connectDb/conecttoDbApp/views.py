from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

# Create your views here.
def home(request):
    body = json.loads(request.body)
    nameee = body['name']
    ageee = body['age']
    emmmmail = body['email']
    
    empObj = Employee(name =nameee , email = emmmmail, age = ageee)
    empObj.save()

    return JsonResponse({
        "message":"data saved successfully",
        "data" : body
    })
