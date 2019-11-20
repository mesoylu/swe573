from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .services import *
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# def login(request):
#     data = list(UserService.login("eleman"))
#     return JsonResponse(data, safe=False)
#
#
# @csrf_exempt
# def wiki(request):
#     query = request.POST.get("query", "")
#     data = WikidataService.query(query)
#     return JsonResponse(data, safe=False)
#
#
# def getCommunity(request, name):
#     data = list(CommunityService.getCommunity(name))
#     return JsonResponse(data, safe=False)
#
#
# def getCommunityMembers(request, name):
#     data = list(CommunityService.getCommunityMembers(name))
#     return JsonResponse(data, safe=False)
#
#
# def getCommunityDataTypes(request, name):
#     data = list(CommunityService.getCommunityDataTypes(name))
#     return JsonResponse(data, safe=False)
#
#
# def getCommunityDataFields(request, name):
#     data = list(CommunityService.getCommunityDataFields(name))
#     return JsonResponse(data, safe=False)
#
#
# def getCommunityPosts(request, name):
#     data = list(CommunityService.getCommunityPosts(name))
#     return JsonResponse(data, safe=False)
#
#
# def getUser(request, username):
#     data = list(UserService.getUser(username))
#     return JsonResponse(data, safe=False)
#
#
# def getPost(request, url):
#     data = list(PostService.getPost(url))
#     return JsonResponse(data, safe=False)

def getAllCommunities(request):
    data = list(CommunityService.get_all_communities())
    return JsonResponse(data, safe=False)


class CommunityViews:

    @csrf_exempt
    def index(request):
        if request.method == 'GET':
            order = request.GET.get('order','-date_created')
            data = list(CommunityService.get_all_communities(order))
            return JsonResponse(data, safe=False)
        # elif request.method == 'POST':
        #    return JsonResponse('elelele', safe=False)

    def community(request,name):
        if request.method == 'GET':
            data = list(CommunityService.get_community(name))
            return JsonResponse(data, safe=False)

    def members(request,name):
        if request.method == 'GET':
            order = request.GET.get('order', '-membership__date_joined')
            data = list(CommunityService.get_members(name,order))
            return JsonResponse(data, safe=False)

    def data_types(request,name):
        if request.method == 'GET':
            order = request.GET.get('order', 'name')
            data = list(CommunityService.get_data_types(name,order))
            return JsonResponse(data, safe=False)

    def posts(request,name):
        order = request.GET.get('order', '-date_created')
        data = list(CommunityService.get_posts(name, order))
        return JsonResponse(data, safe=False)