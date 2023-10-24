from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *

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
    body = json.loads(request.body)

    uname = body['username']
    pswrd = body['password']
    emailllll = body['email']

    checkUsename = User.objects.filter(username = uname)
    if checkUsename.exists():
        return JsonResponse({
            "message":"Username is already exists, please change your username"
        })
    
    checkEmail = User.objects.filter(email = emailllll)
    if checkEmail.exists():
        return JsonResponse({
            "message":"Email  already exists, please login with your username and password"
        })
    

    userSave = User.objects.create(username = uname, email = emailllll, password  = pswrd)

    return JsonResponse({
        "message":"user successfully creeated"
    })


@csrf_exempt
def login(request):
    body = json.loads(request.body)

    uname = body['username']
    pswrd = body['password']

    
    checkUsename = User.objects.filter(username = uname)
    if checkUsename.exists():
        user = User.objects.get(username = uname)
        if pswrd == user.password:
            return JsonResponse({
                "message":"login successfull"
            })
        else:
            return JsonResponse({
                "message":"please enter corrrect password"
            })