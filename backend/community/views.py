from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .services import *


# Create your views here.
def login(request):
    data = list(UserService.login("eleman"))
    return JsonResponse(data,safe=False)

def getCommunity(request,url):
    data = list(CommunityService.getCommunity(url))
    return JsonResponse(data, safe=False)