from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .services import *


# Create your views here.
def login(request):
    data = list(UserService.login("eleman"))
    return JsonResponse(data,safe=False)

def getCommunity(request,community_id):
    data = list(CommunityService.getCommunity(community_id))
    return JsonResponse(data, safe=False)