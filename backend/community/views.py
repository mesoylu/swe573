from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .services import *
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def login(request):
    data = list(UserService.login("eleman"))
    return JsonResponse(data,safe=False)

@csrf_exempt
def wiki(request):
    query = request.POST.get("query","")
    data = WikidataService.query(query)
    return JsonResponse(data, safe=False)

@csrf_exempt
def wikiItem(request):
    query = request.POST.get("query","")
    data = WikidataService.getItem(query)
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