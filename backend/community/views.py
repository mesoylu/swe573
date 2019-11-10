from django.http import HttpResponse
from django.shortcuts import render
from .services import UserService

# Create your views here.
def login(request):
    data = list(UserService.login("eleman"))
    return JsonResponse(data,safe=False)
