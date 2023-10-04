from django.urls import path
from .views import saving

urlpatterns = [
    path('savingSomething/', saving)
]
