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