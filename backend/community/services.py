from .models import *
from .serializations import *
from qwikidata.sparql import (get_subclasses_of_item, return_sparql_query_results)


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

    def create(data,file):
        user = User()
        user.username = data['username']
        user.password = data['password']
        user.image = file['image']
        user.email = data['email']
        user.save()
        return user

    def update(username,data):
        u = User.objects.get(username=username)
        email = data.get('email', '')
        if email != '':
            u.email = email
        image = data.get('image')
        if image != '':
            u.image = image
        u.save()
        return '/u/' + username

    def archive(username):
        # todo think about the scenario, when a user is archived, what happens with his/her posts
        u = User.objects.get(username=username)
        u.is_archived = True
        u.save()
        return '/u/'

    def get_data_types(username, order):
        data_types = DataType.objects.order_by(order).filter(creator__username=username)
        return DataTypeSerializer(data_types, many=True).data

    def get_posts(username,order):
        posts = Post.objects.order_by(order).filter(creator__username=username)
        return PostSerializer(posts, many=True).data


class CommunityService:

    def get_all(order):
        communities = Community.objects.filter(is_archived=False).order_by(order).all()
        return CommunitySerializer(communities, many=True).data

    def get(name):
        community = Community.objects.filter(name=name)
        return CommunitySerializer(community, many=True).data

    def get_members(name,order):
        return Community.objects.filter(name=name).order_by(order).values(
            'members__id',
            'members__username',
            'members__date_registered',
            'membership__date_joined'
        )

    def get_posts(name,order):
        posts = Post.objects.order_by(order).filter(community__name=name)
        return PostSerializer(posts, many=True).data

    def create(data,image):
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

    def subscribe(name,user_id):
        m = Membership()
        m.community = Community.objects.get(name=name)
        m.user = User.objects.get(pk=user_id)
        m.save()
        return '/c/' + name

    def unsubscribe(name,user_id):
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
        return PostSerializer(post,many=True).data

    def update(url, data):
        p = Post.objects.get(url=url)
        body = data.get('body', '')
        if body != '':
            p.body = body
        fields = data.get('fields', '')
        if fields != '':
            p.fields = fields
        p.save()
        return '/p/' + url

    def archive(url):
        p = Post.objects.get(url=url)
        p.is_archived = True
        p.save()
        return '/p/'

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
        dt.fields = data['fields']
        dt.tags = data['tags']
        dt.creator = user
        dt.community = community
        dt.save()
        return '/c/' + name

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
        dt = DataType.objects.get(creator__pk=user_id,pk=id)
        if dt is not None:
            dt.is_archived = True
            dt.save()
        return {"success": True}