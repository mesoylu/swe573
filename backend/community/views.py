from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.utils import json

from .services import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout


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

def index(request):
    if 'current_community' in request.session:
        del request.session['current_community']
    return render(request, 'community/index.html')

@csrf_exempt
def get_fieldform(request):
    if request.method == 'POST':
        index = request.POST.get('index')
        return render(request, 'community/partials/field_form.html', {'index': index})

class CommunityViews:

    @csrf_exempt
    def index(request):
        if request.method == 'GET':
            order = request.GET.get('order','-date_created')
            data = list(CommunityService.get_all(order))
            # return JsonResponse(data, safe=False)
            return render(request, 'community/communities.html',{'communities': data})
        # elif request.method == 'POST':
        #    return JsonResponse('elelele', safe=False)

    @api_view(["PATCH","GET","DELETE"])
    def community(request,name):
        if request.method == 'GET':
            data = list(CommunityService.get(name))
            request.session['current_community'] = name
            # return JsonResponse(data, safe=False)
            # todo had to give the data as [0], because of serialization
            return render(request, 'community/view_community.html', {'community': data[0]})
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

    # @api_view(["POST", "GET", "DELETE"])
    @csrf_exempt
    def members(request,name):
        if request.method == 'GET':
            order = request.GET.get('order', '-membership__date_joined')
            data = list(CommunityService.get_members(name,order))
            return JsonResponse(data, safe=False)
        if request.method == 'POST':
            # todo this is a dummy data for writing a session parameter
            user_id = request.session['user_id']
            redirect_url = CommunityService.subscribe(name,user_id)
            return redirect(redirect_url)
        if request.method == 'DELETE':
            user_id = request.session['user_id']
            CommunityService.unsubscribe(name, user_id)
            return JsonResponse({'Success': True})

    @csrf_exempt
    def data_types(request,name):
        if request.method == 'GET':
            order = request.GET.get('order', 'name')
            data = list(DataTypeService.get_all(name,order))
            return JsonResponse(data, safe=False)
        if request.method == 'POST':
            try:
                data = request.POST.copy()
                # data.image = request.FILES.get('image')
                # todo this is a dummy data for writing a session parameter
                user_id = request.session['user_id']
                redirect_url = DataTypeService.create(name, data, user_id)
                return redirect(redirect_url)
            except IntegrityError as e:
                return HttpResponse(e.__cause__)


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
                image = request.FILES.get('image')
                redirect_url = CommunityService.create(data,image)
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


    def data_types(request, username):
        if request.method == 'GET':
            order = request.GET.get('order', 'name')
            data = list(DataTypeService.get_all(username,order))
            return JsonResponse(data, safe=False)

    @api_view(["PATCH", "DELETE"])
    def data_type(request, username, id):
        if request.method == 'PATCH':
            try:
                data = json.loads(request.body)
                # todo this is a dummy data for writing a session parameter
                request.session['user_id'] = 3
                user_id = request.session['user_id']
                response = DataTypeService.update(id, user_id, data)
                return HttpResponse(response)
            except IntegrityError as e:
                return HttpResponse(e.__cause__)
        elif request.method == 'DELETE':
            try:
                # todo this is a dummy data for writing a session parameter
                request.session['user_id'] = 3
                user_id = request.session['user_id']
                response = DataTypeService.archive(id, user_id)
                return HttpResponse(response)
            except IntegrityError as e:
                return HttpResponse(e.__cause__)

    def posts(request,username):
        order = request.GET.get('order', '-date_created')
        data = list(UserService.get_posts(username, order))
        return JsonResponse(data, safe=False)

    def votes(request, username):
        data = list(VoteService.get_all(username))
        return JsonResponse(data, safe=False)

    @csrf_exempt
    def login(request):
        if request.method == 'GET':
            if 'user_id' not in request.session:
                return render(request, 'community/login.html')
            else:
                redirect_url = '/u/' + request.session['username']
                return redirect(redirect_url)
        elif request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            # todo this method is not suitable, should update later
            user = User.objects.get(username=username,password=password)
            if user is not None:
                request.session['username'] = user.username
                request.session['user_id'] = user.id
                redirect_url = '/u/' + user.username
                return redirect(redirect_url)
            else:
                return JsonResponse('User authentication failed!', safe=False)

    # todo logout should be a post method but it is convenient to use get rignt now
    def logout(request):
        if request.method == 'GET':
            #todo instead of flushing using del would be better
            request.session.flush()
        redirect_url = '/'
        return redirect(redirect_url)

    def signup(request):
        if request.method == 'GET':
            if 'user_id' not in request.session:
                return render(request, 'community/signup.html')
            else:
                redirect_url = '/u/' + request.session['username']
                return redirect(redirect_url)
        elif request.method == 'POST':
            try:
                user = User.objects.get(username=request.POST['username'])
            except:
                user = None
            if user is not None:
                return JsonResponse('Username exists!', safe=False)

            try:
                user = User.objects.get(email=request.POST['email'])
            except:
                user = None
            if user is not None:
                return JsonResponse('Email already used on an account!', safe=False)

            u = UserService.create(request.POST, request.FILES)
            request.session['username'] = u.username
            request.session['user_id'] = u.id

            redirect_url = '/u/' + u.username
            return redirect(redirect_url)




class PostViews:

    def index(request):
        if request.method == 'GET':
            order = request.GET.get('order','-date_created')
            data = list(PostService.get_all(order))
            return JsonResponse(data, safe=False)

    @csrf_exempt
    def create(request, name):
        if request.method == 'GET':
            form = PostForm()
            # for key, value in request.session.items():
            #     print('{} => {}'.format(key, value))
            return render(request, 'community/new_post.html', {'form': form})
        elif request.method == 'POST':
            try:
                data = request.POST.copy()
                files = request.FILES.copy()
                redirect_url = PostService.create(name, request.session['user_id'], data, files)
                return redirect(redirect_url)
            except IntegrityError as e:
                return HttpResponse(e.__cause__)

    # todo is the name ok?
    @api_view(["PATCH", "GET", "DELETE"])
    def post(request, url):
        if request.method == 'GET':
            data = list(PostService.get(url))
            # return JsonResponse(data, safe=False)
            return render(request, 'community/view_post.html', {'post': data[0]})
        elif request.method == 'PATCH':
            try:
                data = request.data
                redirect_url = PostService.update(url, data)
                return redirect(redirect_url)
            except IntegrityError as e:
                return HttpResponse(e.__cause__)
        elif request.method == 'DELETE':
            try:
                redirect_url = PostService.archive(url)
                return redirect(redirect_url)
            except IntegrityError as e:
                return HttpResponse(e.__cause__)

    @api_view(["PUT", "DELETE"])
    def vote(request, url):
        if request.method == 'PUT':
            try:
                is_upvote = request.data.get('is_upvote')
                # todo this is a dummy data for writing a session parameter
                request.session['user_id'] = 2
                user_id = request.session['user_id']
                response = VoteService.vote(url, user_id, is_upvote)
                return HttpResponse(response)
            except IntegrityError as e:
                return HttpResponse(e.__cause__)
        elif request.method == 'DELETE':
            try:
                user_id = request.session['user_id']
                response = VoteService.unvote(url, user_id)
                return HttpResponse(response)
            except IntegrityError as e:
                return HttpResponse(e.__cause__)


class DataTypeViews:

    def create(request, name):
        if request.method == 'GET':
            form = DataTypeForm()
            # for key, value in request.session.items():
            #     print('{} => {}'.format(key, value))
            return render(request, 'community/new_datatype.html', {'form': form})
