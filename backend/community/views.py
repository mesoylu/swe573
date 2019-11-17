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

def getCommunity(request,name):
    data = list(CommunityService.getCommunity(name))
    return JsonResponse(data, safe=False)

def getCommunityMembers(request,name):
    data = list(CommunityService.getCommunityMembers(name))
    return JsonResponse(data, safe=False)

def getCommunityDataTypes(request,name):
    data = list(CommunityService.getCommunityDataTypes(name))
    return JsonResponse(data, safe=False)

def getCommunityDataFields(request,name):
    data = list(CommunityService.getCommunityDataFields(name))
    return JsonResponse(data, safe=False)

def getCommunityPosts(request,name):
    data = list(CommunityService.getCommunityPosts(name))
    return JsonResponse(data, safe=False)