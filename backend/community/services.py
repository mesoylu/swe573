from .models import *


# todo the methods from class diagram will be written here
# todo learn how to use sessions in order to use logged in user id type of thing
class UserService:

    def login(data):
        return User.objects.values()


class CommunityService:

    def getCommunity(url):
        return Community.objects.filter(url=url).values(
            'id',
            'name',
            'description',
            'creator__username',
            'date_created'
        )

    def getCommunityMembers(url):
        return Community.objects.filter(url=url).values(
            'members__id',
            'members__username',
            'members__date_registered'
        )

    def getCommunityDataTypes(url):
        return Community.objects.filter(url=url).values(
            'datatype__id',
            'datatype__title',
            'datatype__body'
        )

    def getCommunityDataFields(url):
        # todo is it possible to use Community here or should i use DataField model instead
        return Community.objects.filter(url=url).values(
            'datafield__id',
            'datafield__type__name',
            'datafield__is_required',
            'datafield__wikidata_item'
        )
        #data = Community.objects.filter(url=url).values(
        #    'id'
        #)
        #return DataField.objects.filter(id=data[0]).values()

