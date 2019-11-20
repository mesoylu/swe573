from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

# urlpatterns = \
#     [
#         path('login', views.login),
#         path('c/<name>/', include([
#             path('', views.getCommunity),
#             path('members/', views.getCommunityMembers),
#             path('datatypes/', views.getCommunityDataTypes),
#             path('datafields/', views.getCommunityDataFields),
#             path('posts/', views.getCommunityPosts),
#         ])),
#         path('u/<username>/', include([
#             path('', views.getUser),
#         ])),
#         path('p/<url>/', include([
#             path('', views.getPost),
#         ])),
#         path('wiki', views.wiki)
#     ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = \
    [
        # todo homepage
        # path('', views.index),
        # todo community related views
        path('c/', include([
            # todo GET getAllCommunities, POST createCommunity
            # path('', views.Communities),
            path('<name>', include([
                # todo GET getCommunity, PATCH updateCommunity, DELETE deleteCommunity
                # path('', views.Community),
                # todo GET getMembers, POST subscribe
                # path('members/', views.CommunityMembers),
                # todo GET getDataTypes, POST createDataType
                # path('datatypes/', views.getCommunityDataTypes),
                # todo GET getDataFields, POST createDataField
                # path('datafields/', views.getCommunityDataFields),
                # todo GET getCommunityPosts
                # path('posts/', views.getCommunityPosts)
            ]))
        ])),
        # todo user related views
        path('u/', include([
            # todo GET getAllUsers
            # path('', views.Users),
            # todo GET loginform?, POST login
            # path('login', views.Login),
            # todo GET signupform?, POST signup
            # path('signup', views.Signup),
            path('<username>', include([
                # todo GET getUser, PATCH updateUser, DELETE deleteUser
                # path('', views.User),
                # todo GET getDataTypes, POST createDataType
                # path('datatypes/', views.getUserDataTypes),
                # todo GET getDataFields, POST createDataField
                # path('datafields/', views.getUserDataFields),
                # todo GET getCommunityPosts
                # path('posts/', views.getUserPosts)
                # todo GET lastVotedByUser
                # path('votes/', views.getUserVotes)
            ])),
        ])),
        # todo post related views
        path('p/', include([
            # todo GET getAllPosts
            # path('', views.Posts),
            path('<url>', include([
                # todo GET getPost, PATCH updatePost, DELETE deletePost
                # path('', views.Post),
                # todo POST vote, PATCH updateVote, DELETE deleteVote
                # path('vote', views.Vote),
            ]))
        ])),
        # todo wikidata related views
        path('wiki', views.wiki)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    # todo https://docs.djangoproject.com/en/2.2/howto/static-files/ it is not suitable on prod

