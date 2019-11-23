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

    def login(data):
        return User.objects.values()

    def getUser(username):
        # return User.objects.filter(username=username).values_list(
        #     'username',
        #     'membership__community__name'
        # )
        user = User.objects.filter(username=username)
        return UserSerializer(user, many=True).data

    def get_all_users(order):
        users = User.objects.filter(is_archived=False).order_by(order).all()
        return UserSerializer(users, many=True).data


class CommunityService():

    def get_all_communities(order):
        communities = Community.objects.filter(is_archived=False).order_by(order).all()
        return CommunitySerializer(communities, many=True).data

    def get_community(name):
        community = Community.objects.filter(name=name)
        return CommunitySerializer(community, many=True).data

    def get_members(name,order):
        return Community.objects.filter(name=name).order_by(order).values(
            'members__id',
            'members__username',
            'members__date_registered',
            'membership__date_joined'
        )

    def get_data_types(name,order):
        data_types = DataType.objects.order_by(order).filter(community__name=name)
        return DataTypeSerializer(data_types, many=True).data

    def get_posts(name,order):
        posts = Post.objects.order_by(order).filter(community__name=name)
        return PostSerializer(posts, many=True).data

    def create(data):
        c = Community()
        c.name = data.get('name', '')
        c.description = data.get('description', '')
        c.image = data.get('image')
        creator = User.objects.get(pk=data.get('creator', ''))
        c.creator = creator
        c.save()
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



    # def getCommunity(name):
    #     # return Community.objects.filter(name=name).values(
    #     #     'id',
    #     #     'name',
    #     #     'description',
    #     #     'creator__username',
    #     #     'date_created'
    #     # )
    #     community = Community.objects.filter(name=name)
    #     return CommunitySerializer(community, many=True).data
    #
    # # todo should i know when member joined a community
    # def getCommunityMembers(name):
    #     return Community.objects.filter(name=name).values(
    #         'members__id',
    #         'members__username',
    #         'members__date_registered'
    #     )
    #
    # def getCommunityDataTypes(name):
    #     return Community.objects.filter(name=name).values(
    #         'datatype__id',
    #         'datatype__title',
    #         'datatype__body',
    #         'datatype__fields'
    #     )
    #
    # def getCommunityDataFields(name):
    #     # todo is it possible to use Community here or should i use DataField model instead
    #     return Community.objects.filter(name=name).values(
    #         'datafield__id',
    #         'datafield__name',
    #         'datafield__type',
    #         'datafield__is_required',
    #         'datafield__wikidata_item__item'
    #     )
    #     # data = Community.objects.filter(name=name).values(
    #     #    'id'
    #     # )
    #     # return DataField.objects.filter(id=data[0]).values()
    #
    # def getCommunityPosts(name):
    #     return Community.objects.filter(name=name).values(
    #         'field_value'
    #     )



class PostService:

    def getPost(url):
        post = Post.objects.filter(url=url)
        return PostSerializer(post,many=True).data