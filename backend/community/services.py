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


class CommunityService:

    def getCommunity(name):
        return Community.objects.filter(name=name).values(
            'id',
            'name',
            'description',
            'creator__username',
            'date_created'
        )

    # todo should i know when member joined a community
    def getCommunityMembers(name):
        return Community.objects.filter(name=name).values(
            'members__id',
            'members__username',
            'members__date_registered'
        )

    def getCommunityDataTypes(name):
        return Community.objects.filter(name=name).values(
            'datatype__id',
            'datatype__title',
            'datatype__body',
            'datatype__fields'
        )

    def getCommunityDataFields(name):
        # todo is it possible to use Community here or should i use DataField model instead
        return Community.objects.filter(name=name).values(
            'datafield__id',
            'datafield__name',
            'datafield__type',
            'datafield__is_required',
            'datafield__wikidata_item__item'
        )
        # data = Community.objects.filter(name=name).values(
        #    'id'
        # )
        # return DataField.objects.filter(id=data[0]).values()

    def getCommunityPosts(name):
        return Community.objects.filter(name=name).values(
            'field_value'
        )
