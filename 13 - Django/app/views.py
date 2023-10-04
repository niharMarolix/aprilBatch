from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserInfo
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
def saving(request):
    body = json.loads(request.body)
    naam = body['name']
    emaaal = body['e']
    teelapjone = body['tel']

    ui = UserInfo(name=naam, email=emaaal, telephone=teelapjone)
    ui.save()
    return JsonResponse({
        "message":"form has been submited"
    })
