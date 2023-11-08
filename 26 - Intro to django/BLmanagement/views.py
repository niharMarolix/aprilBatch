from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics,status,views,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

@api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
def createAuthor(request):
    try:
        if request.user.username == "":
            raise Exception("user is not signed in")
        if request.user.canCreateAuthor == False:
            raise Exception("User is not authorised")
        else:
            requestBodyToDict = json.loads(request.body)

            try:
                emailFromPostman = requestBodyToDict['email']

                checkEmailExists = Author.objects.filter(email = emailFromPostman).exists()

                if checkEmailExists == True:
                    raise Exception("Auhor is already added to the database")
                else:
                    nameFromPostmanBody = requestBodyToDict['name']
                    email = requestBodyToDict['email']

                    savingNameToDb = Author(name = nameFromPostmanBody, email=email)
                    savingNameToDb.save()

                    return JsonResponse({
                        "message":f"{nameFromPostmanBody} added to Author table"
                    })

            except Exception as ex:
                return JsonResponse({
                    "message":str(ex),
                    "status":"failed"
                }, status = status.HTTP_409_CONFLICT)

            

    except Exception as ex:
        return JsonResponse({
            "message":str(ex),
            "status":'falied'
        }, status = status.HTTP_401_UNAUTHORIZED)
    
    

@csrf_exempt
def createBooks(request):
    requestBodyToDict = json.loads(request.body)

    authorId = requestBodyToDict['author_id']
    authorName = Author.objects.get(id = authorId).name

    Books = requestBodyToDict['title']

    bookLists = []

    for  book in Books:
        bookLists.append(book)
        newBook = Book.objects.create(title = book, author_id = authorId)


    return JsonResponse({
        "message": f"{bookLists} of {authorName} added successfully"
    })


def getBooknamesFromAuthor(request):
    authId = (json.loads(request.body))['authorId']

    authorName = Author.objects.get(id = authId).name

    booksQuerySet = Book.objects.filter(author_id = authId)

    bookLists = []

    for  book in booksQuerySet:
        bookLists.append(book.title)
        newBook = Book.objects.create(title = book, author_id = authId)

    return JsonResponse({
        "message": f"{bookLists} of {authorName} retrieved successfully"
    })


@csrf_exempt
def updateAuthor(request):
    authId = (json.loads(request.body))['authorId']
    CN = (json.loads(request.body))['changedName']
    
    authObj = Author.objects.get(id = authId)
    olname = authObj.name
    newName = Author.objects.update(name = CN)
    
    return JsonResponse({
        "message":f"{olname} is replaced by {CN}"
    })

@csrf_exempt
def deleteAuthor(request):
    authId = (json.loads(request.body))['authorId']
    authObj = Author.objects.get(id = authId)
    name = authObj.name
    authObj.delete()

    return JsonResponse({
        "message":f"{name} is deleted from the author table"
    })

@csrf_exempt
def register(request):
    try:
        if request.method != "POST":
            raise Exception("method not allowed", status.HTTP_405_METHOD_NOT_ALLOWED)
        
        else:
            data = json.loads(request.body)

            esmail = data["email"]
            usalname = data["username"]
            passworddddd = data["password"]
            canCreateAutor = data["canCreateAuthor"]

            if not esmail or not usalname or not passworddddd:
                raise Exception("Data not passed or incorrect data passed", status.HTTP_400_BAD_REQUEST)
            
            else:
                user = User.objects.create_user(username = usalname, password = passworddddd, email = esmail, canCreateAuthor = canCreateAutor)
                user.save()

                return JsonResponse({
                    "status":"Success",
                    "message":f"User {usalname} registered"
                    
                }, status = status.HTTP_201_CREATED)
    
    except Exception as ex:
        return JsonResponse({
            "status":"failed",
            "message":str(ex)
        })
    
@csrf_exempt
def login(request):
    try:
        if request.method != "POST":
            raise Exception("method not allowed", status.HTTP_405_METHOD_NOT_ALLOWED)
        
        else:
            data = json.loads(request.body)
            usalname = data["username"]
            passworddddd = data["password"]

            if not usalname or not passworddddd:
                raise Exception("Data not passed or incorrect data passed", status.HTTP_400_BAD_REQUEST)
            
            else:
                user = authenticate(request, username= usalname, password = passworddddd)

                if user is not None:
                    refrest = RefreshToken.for_user(user)

                    return JsonResponse({
                        "refreshToken":str(refrest),
                        "accesstoken":str(refrest.access_token)
                    })


            
    except Exception as ex:
        return JsonResponse({
            "status":"failed",
            "message":str(ex)
        })


