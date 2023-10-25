from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
@csrf_exempt
def createAuthor(request):
    requestBodyToDict = json.loads(request.body)

    nameFromPostmanBody = requestBodyToDict['name']

    savingNameToDb = Author(name = nameFromPostmanBody)
    savingNameToDb.save()

    return JsonResponse({
        "message":f"{nameFromPostmanBody} added to Author table"
    })

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
    if request.method != "POST":
        return JsonResponse({
            "message":"method not supported",
            "status":"failed"
        }, status = status.HTTP_405_METHOD_NOT_ALLOWED)
    
    else:
        data = json.loads(request.body)
        emaillllll = data['email']
        usernameeeeeee = data['username']
        passwordddddddd = data['password']

        if not emaillllll or not usernameeeeeee or not passwordddddddd:
            return JsonResponse({
                "message":"input fields should not be empty"
            }, status = status.HTTP_400_BAD_REQUEST)
        
        else:
            user = User.objects.create_user(email =emaillllll, username =usernameeeeeee, password = passwordddddddd  )
            user.save()

            return JsonResponse({
                "message":f"User {usernameeeeeee} registered successfully"
            }, status = status.HTTP_201_CREATED)

@csrf_exempt
def login(request):
    if request.method != "POST":
        return JsonResponse({
            "message":"method not supported",
            "status":"failed"
        }, status = status.HTTP_405_METHOD_NOT_ALLOWED)
    
    else:
        data = json.loads(request.body)
        usernameeeeeee = data['username']
        passwordddddddd = data['password']

        if  not usernameeeeeee or not passwordddddddd:
            return JsonResponse({
                "message":"input fields should not be empty"
            }, status = status.HTTP_400_BAD_REQUEST)
        
        else:
            user = authenticate(request, username = usernameeeeeee, password = passwordddddddd)

            if user is not None:
                refresf = RefreshToken.for_user(user)

                return JsonResponse({
                    "access-token":str(refresf.access_token),
                    "refresh-token":str(refresf)
                })


