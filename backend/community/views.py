from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .services import *
from pprint import pprint


# Create your views here.
def login(request):
    data = list(UserService.login("eleman"))
    return JsonResponse(data,safe=False)

def wiki(request):
    data = WikidataService.query(WikidataService)
    return JsonResponse(data, safe=False)

def getCommunity(request,url):
    data = list(CommunityService.getCommunity(url))
    return JsonResponse(data, safe=False)

def getCommunityMembers(request,url):
    data = list(CommunityService.getCommunityMembers(url))
    return JsonResponse(data, safe=False)

def getCommunityDataTypes(request,url):
    data = list(CommunityService.getCommunityDataTypes(url))
    return JsonResponse(data, safe=False)

def getCommunityDataFields(request,url):
    data = list(CommunityService.getCommunityDataFields(url))
    return JsonResponse(data, safe=False)

def getCommunityPosts(request,url):
    data = list(CommunityService.getCommunityPosts(url))
    return JsonResponse(data, safe=False)