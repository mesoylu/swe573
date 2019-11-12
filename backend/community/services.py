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
