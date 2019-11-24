from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .services import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

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
            data = list(CommunityService.get_all(order))
            return JsonResponse(data, safe=False)
        # elif request.method == 'POST':
        #    return JsonResponse('elelele', safe=False)

    @api_view(["PATCH","GET","DELETE"])
    def community(request,name):
        if request.method == 'GET':
            data = list(CommunityService.get(name))
            return JsonResponse(data, safe=False)
        if request.method == 'PATCH':
            try:
                data = request.data
                redirect_url = CommunityService.update(name, data)
                return redirect(redirect_url)
            except IntegrityError as e:
                return HttpResponse(e.__cause__)
        if request.method == 'DELETE':
            try:
                redirect_url = CommunityService.archive(name)
                return redirect(redirect_url)
            except IntegrityError as e:
                return HttpResponse(e.__cause__)

    @api_view(["POST", "GET", "DELETE"])
    def members(request,name):
        if request.method == 'GET':
            order = request.GET.get('order', '-membership__date_joined')
            data = list(CommunityService.get_members(name,order))
            return JsonResponse(data, safe=False)
        if request.method == 'POST':
            # todo this is a dummy data for writing a session parameter
            request.session['user_id'] = 3
            user_id = request.session['user_id']
            redirect_url = CommunityService.subscribe(name,user_id)
            return redirect(redirect_url)
        if request.method == 'DELETE':
            user_id = request.session['user_id']
            redirect_url = CommunityService.unsubscribe(name, user_id)
            return redirect(redirect_url)

    def data_types(request,name):
        if request.method == 'GET':
            order = request.GET.get('order', 'name')
            data = list(CommunityService.get_data_types(name,order))
            return JsonResponse(data, safe=False)

    def posts(request,name):
        order = request.GET.get('order', '-date_created')
        data = list(CommunityService.get_posts(name, order))
        return JsonResponse(data, safe=False)

    @csrf_exempt
    def create(request):
        if request.method == 'GET':
            form = CommunityForm()
            return render(request, 'community/new_community.html', {'form': form})
        elif request.method == 'POST':
            try:
                data = request.POST.copy()
                data.image = request.FILES.get('image')
                redirect_url = CommunityService.create(data)
                return redirect(redirect_url)
            except IntegrityError as e:
                return HttpResponse(e.__cause__)


class UserViews:
    def index(request):
        if request.method == 'GET':
            order = request.GET.get('order','-date_registered')
            data = list(UserService.get_all(order))
            return JsonResponse(data, safe=False)

    @api_view(["PATCH", "GET", "DELETE"])
    def user(request, username):
        if request.method == 'GET':
            data = list(UserService.get(username))
            return JsonResponse(data, safe=False)
        elif request.method == 'PATCH':
            try:
                data = request.data
                redirect_url = UserService.update(username, data)
                return redirect(redirect_url)
            except IntegrityError as e:
                return HttpResponse(e.__cause__)
        elif request.method == 'DELETE':
            try:
                redirect_url = UserService.archive(username)
                return redirect(redirect_url)
            except IntegrityError as e:
                return HttpResponse(e.__cause__)

    def data_types(request,username):
        if request.method == 'GET':
            order = request.GET.get('order', 'name')
            data = list(UserService.get_data_types(username,order))
            return JsonResponse(data, safe=False)

    def posts(request,username):
        order = request.GET.get('order', '-date_created')
        data = list(UserService.get_posts(username, order))
        return JsonResponse(data, safe=False)


class PostViews:

    def index(request):
        if request.method == 'GET':
            order = request.GET.get('order','-date_created')
            data = list(PostService.get_all(order))
            return JsonResponse(data, safe=False)