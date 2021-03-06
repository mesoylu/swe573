import datetime

from .models import *
from .serializations import *
from qwikidata.sparql import (get_subclasses_of_item, return_sparql_query_results)
from qwikidata.entity import WikidataItem, WikidataLexeme, WikidataProperty
from qwikidata.linked_data_interface import get_entity_dict_from_api


class SearchService:

    def basic_search(query):
        response = {}
        communities = []
        posts = []
        users = []
        c_set = Community.objects.filter(name__icontains=query)
        i = 0
        for c in c_set:
            community = dict()
            community['name'] = c.name
            if c.image != '':
                community['image'] = c.image.url
            communities.append(community)
            i = i + 1
        u_set = User.objects.filter(username__icontains=query)
        i = 0
        for u in u_set:
            user = {}
            user['username'] = u.username
            if u.image != '':
                user['image'] = u.image.url
            users.append(user)
            i = i + 1
        p_set = Post.objects.filter(title__icontains=query)
        i = 0
        for p in p_set:
            post = {}
            post['title'] = p.title
            post['url'] = p.url
            posts.append(post)
            i = i + 1
        response['communities'] = communities
        response['posts'] = posts
        response['users'] = users
        return response


class WikidataService:

    def query(query):
        # send any sparql query to the wikidata query service and get full result back
        # here we use an example that counts the number of humans
        sparql_query = """
        SELECT distinct ?item ?itemLabel ?itemDescription WHERE{  
          ?item rdfs:label "%s"@en.  
          SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }  
        }
        """ % query
        return return_sparql_query_results(sparql_query)

    def get_item(itemId):
        item = get_entity_dict_from_api(itemId)
        return item


# todo the methods from class diagram will be written here
# todo learn how to use sessions in order to use logged in user id type of thing
class UserService:

    def getUser(username):
        # return User.objects.filter(username=username).values_list(
        #     'username',
        #     'membership__community__name'
        # )
        user = User.objects.filter(username=username)
        return UserSerializer(user, many=True).data

    def get_all(order):
        users = User.objects.filter(is_archived=False).order_by(order).all()
        return UserSerializer(users, many=True).data

    def get(username):
        user = User.objects.filter(username=username)
        return UserSerializer(user, many=True).data

    def create(data, file):
        user = User()
        user.username = data['username']
        user.password = data['password']
        user.image = file['image']
        user.email = data['email']
        user.save()
        return user

    def update(username, data, files):
        u = User.objects.get(username=username)
        email = data.get('email', '')
        if email != '':
            u.email = email
        image = files.get('image')
        if image is not None:
            u.image = image
        u.save()
        return '/u/' + username

    def archive(username, session_username):
        # todo think about the scenario, when a user is archived, what happens with his/her posts
        u = User.objects.get(username=username)
        if username == session_username:
            u.is_archived = True
            u.save()
            return '/u/'
        else:
            return '/u/' + username

    def get_data_types(username, order):
        data_types = DataType.objects.order_by(order).filter(creator__username=username)
        return DataTypeSerializer(data_types, many=True).data

    def get_posts(username, order):
        posts = Post.objects.order_by(order).filter(creator__username=username)
        return PostSerializer(posts, many=True).data


class CommunityService:

    def get_all(order):
        communities = Community.objects.filter(is_archived=False).order_by(order).all()
        return CommunitySerializer(communities, many=True).data

    def get(name):
        community = Community.objects.filter(name=name)
        return CommunitySerializer(community, many=True).data

    def get_members(name, order):
        return Community.objects.filter(name=name).order_by(order).values(
            'members__id',
            'members__username',
            'members__date_registered',
            'membership__date_joined'
        )

    def get_posts(name, order):
        posts = Post.objects.order_by(order).filter(community__name=name)
        return PostSerializer(posts, many=True).data

    def create(data, image):
        c = Community()
        c.name = data.get('name', '')
        c.description = data.get('description', '')
        c.image = image
        creator = User.objects.get(pk=data.get('creator', ''))
        c.creator = creator
        c.save()
        c.members.set([creator.id])
        return '/c/' + c.name

    def update(name, data):
        c = Community.objects.get(name=name)
        description = data.get('description', '')
        if description != '':
            c.description = description
        image = data.get('image')
        if image != '':
            c.image = image
        c.save()
        return '/c/' + c.name

    def archive(name):
        c = Community.objects.get(name=name)
        c.is_archived = True
        c.save()
        return '/c/'

    def subscribe(name, user_id):
        m = Membership()
        m.community = Community.objects.get(name=name)
        m.user = User.objects.get(pk=user_id)
        m.save()
        return '/c/' + name

    def unsubscribe(name, user_id):
        c = Community.objects.get(name=name)
        u = User.objects.get(pk=user_id)
        m = Membership.objects.get(user=u, community=c)
        m.delete()
        return '/c/' + name


class PostService:

    def get_all(order):
        posts = Post.objects.filter(is_archived=False).order_by(order).all()
        return PostSerializer(posts, many=True).data

    def get(url):
        post = Post.objects.filter(url=url)
        return PostSerializer(post, many=True).data

    def create(url, user_id, data, files):
        p = Post()
        c = Community.objects.get(name=url)
        u = User.objects.get(id=user_id)
        p.community = c
        p.creator = u
        p.upvote_count = 0
        p.downvote_count = 0
        p.title = data.get('title')
        p.body = data.get('body')
        if 'data_type' in data:
            p.data_type_id = data.get('data_type')
            p.fields = PostService.field_values(p.data_type_id, data)
        p.save()
        return '/p/' + p.url

    def field_values(data_type_id, data):
        dt = DataType.objects.get(pk=data_type_id)
        fields = dt.fields
        post_fields = []
        for field in fields:
            field_name = 'data_field_' + field['label']
            if field['type'] == 'integer':
                field['value'] = int(data.get(field_name))
            elif field['type'] == 'float':
                field['value'] = float(data.get(field_name))
            elif field['type'] == 'boolean':
                field['value'] = bool(int(data.get(field_name)))
            # elif field['type'] == 'date':
            #     date_time_obj = datetime.strptime(data.get(field_name), '%Y-%m-%d')
            #     field['value'] = date_time_obj.date()
            elif field['type'] == 'geolocation':
                latitude = field_name + '_lat'
                field['value']['latitude'] = float(data.get(latitude))
                longitude = field_name + '_long'
                field['value']['longitude'] = float(data.get(longitude))
            elif field['type'] == 'multiple' or field['type'] == 'list':
                multiple = field_name
                field['value'] = data.getlist(multiple)
            elif field['type'] == 'video' or field['type'] == 'audio' or field['type'] == 'uri':
                title = field_name + '_title'
                field['value']['title'] = data.get(title)
                field['value']['url'] = data.get(field_name)
            else:
                field['value'] = data.get(field_name)
            post_fields.append(field)
        return post_fields

    def update(url, data):
        p = Post.objects.get(url=url)
        # body = data.get('body', '')
        # if body != '':
        #     p.body = body
        # fields = data.get('fields', '')
        # if fields != '':
        #     p.fields = fields
        p.body = data.get('body')
        p.fields = PostService.field_values(p.data_type_id, data)
        p.save()
        return '/p/' + url

    def archive(url, user_id):
        p = Post.objects.get(url=url)
        u = User.objects.get(pk=user_id)
        if p.creator_id == user_id:
            p.is_archived = True
            p.save()
            return '/u/' + u.username
        else:
            return '/p/' + url

    def update_fields(data):
        post_fields = data[0]['fields']
        data_type = list(DataTypeService.get_from_name(data[0]['data_type']))
        data_type_fields = data_type[0]['fields']
        i = 0
        for field in data_type_fields:
            for post_field in post_fields:
                if field['label'] == post_field['label']:
                    field['value'] = post_field['value']
                    # post_field.remove()
        return data_type_fields

    def search(url, data):
        posts = Post.objects.all()
        data_type_fields = None
        if 'data_type' in data:
            posts = posts.filter(data_type__id=data.get('data_type'))
            data_type = DataType.objects.get(pk=data.get('data_type'))
            data_type_fields = data_type.fields
        else:
            posts = posts.filter(data_type=None,community__name=url)

        for item in data:
            if item == 'data_type':
                pass
            else:
                if item == 'title':
                    posts = posts.filter(title__icontains=data.get('title'))
                elif item == 'body':
                    posts = posts.filter(body__icontains=data.get('body'))
                else:
                    if data_type_fields is not None:
                        for field in data_type_fields:
                            label = item.replace('data_field_','')
                            if field['label'] == label:
                                if field['type'] == 'float':
                                    posts = posts.filter(fields__contains=[{"label": label, "value": float(data.get(item))}])
                                elif field['type'] == 'integer':
                                    posts = posts.filter(
                                        fields__contains=[{"label": label, "value": int(data.get(item))}])
                                elif field['type'] == 'boolean':
                                    posts = posts.filter(
                                        fields__contains=[{"label": label, "value": bool(int(data.get(item)))}])
                                else:
                                    posts = posts.filter(
                                        fields__contains=[{"label": label, "value": data.get(item)}])
        return PostSerializer(posts, many=True).data


class VoteService:

    def vote(url, user_id, is_upvote):
        user = User.objects.get(pk=user_id)
        post = Post.objects.get(url=url)

        try:
            vote = Vote.objects.get(user=user, post=post)
        except Vote.DoesNotExist:
            vote = None

        if vote is None:
            v = Vote()
            v.user = user
            v.post = post
            v.is_upvote = is_upvote
            v.save()
        elif vote.is_upvote != is_upvote:
            vote.is_upvote = is_upvote
            vote.save()
        return {"success": True}

    def unvote(url, user_id):
        user = User.objects.get(pk=user_id)
        post = Post.objects.get(url=url)
        vote = Vote.objects.get(user=user, post=post)
        vote.delete()
        return {"success": True}

    def get_all(username):
        votes = Vote.objects.order_by('-id').filter(user__username=username)
        return VoteSerializer(votes, many=True).data


class DataTypeService:

    def get_all(name, order):
        data_types = DataType.objects.order_by(order).filter(community__name=name)
        return DataTypeSerializer(data_types, many=True).data

    def create(name, data, user_id):
        user = User.objects.get(pk=user_id)
        community = Community.objects.get(name=name)
        dt = DataType()
        dt.name = data['name']
        dt.description = data['description']
        fields = []
        if int(data['has_fields']) > 0:
            i = 0
            while i < int(data['has_fields']):
                i += 1
                field_label = 'field_label_' + str(i)
                field_type = 'field_type_' + str(i)
                field_is_required = 'is_required_' + str(i)
                if field_is_required in data:
                    is_required = True
                else:
                    is_required = False
                field = {
                    'label': data[field_label],
                    'type': data[field_type],
                    'is_required': is_required,
                    'value': None,
                    'choices': [],
                    'tags': None
                }
                if data[field_type] == 'enumeration':
                    choice_field = 'choice_values_' + str(i)
                    field['choices'] = data[choice_field].split(',')
                elif data[field_type] == 'multiple':
                    choice_field = 'choice_values_' + str(i)
                    field['choices'] = data[choice_field].split(',')
                elif data[field_type] == 'geolocation':
                    field['value'] = {
                        'latitude': None,
                        'longitude': None
                    }
                elif data[field_type] == 'video' or data[field_type] == 'audio' or data[field_type] == 'uri':
                    field['value'] = {
                        'title': None,
                        'url': None
                    }
                fields.append(field)

        dt.fields = fields
        # dt.tags = data['tags']
        dt.creator = user
        dt.community = community
        dt.save()
        return '/c/' + name

    def get(id):
        dt = DataType.objects.filter(pk=id)
        return DataTypeSerializer(dt, many=True).data

    def get_from_name(name):
        dt = DataType.objects.filter(name=name)
        return DataTypeSerializer(dt, many=True).data

    def update(id, user_id, data):
        dt = DataType.objects.get(pk=id)
        if 'fields' in data:
            dt.fields = data['fields']
        if 'description' in data:
            dt.description = data['description']
        if 'tags' in data:
            dt.tags = data['tags']
        dt.save()
        return {"success": True}

    def archive(id, user_id):
        dt = DataType.objects.get(creator__pk=user_id, pk=id)
        if dt is not None:
            dt.is_archived = True
            dt.save()
        return {"success": True}
