from .models import *


# todo the methods from class diagram will be written here
# todo learn how to use sessions in order to use logged in user id type of thing
class UserService:

    def login(data):
        return User.objects.values()


class CommunityService:

    def getCommunity(community_id):
        return Community.objects.filter(id=community_id).values()