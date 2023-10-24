from django.urls import path
from .views import *

urlpatterns = [
    path('createAuthor',createAuthor),
    path('createBooks',createBooks),
    path('getBooknamesFromAuthor',getBooknamesFromAuthor),
    path('updateAuthor',updateAuthor),
    path('deleteAuthor',deleteAuthor),
    path('register', register),
    path('login', login)
]
