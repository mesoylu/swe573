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
            path('', views.CommunityViews.index),
            path('new', views.CommunityViews.create),
            path('<name>/', include([
                path('', views.CommunityViews.community),
                path('members/', views.CommunityViews.members),
                # todo POST createDataType
                path('datatypes/', views.CommunityViews.data_types),
                # todo GET getDataFields, POST createDataField
                # path('datafields/', views.getCommunityDataFields),
                path('posts/', views.CommunityViews.posts)
            ]))
        ])),
        # todo user related views
        path('u/', include([
            path('', views.UserViews.index),
            # todo GET loginform?, POST login
            # path('login', views.Login),
            # todo GET signupform?, POST signup
            # path('signup', views.Signup),
            path('<username>/', include([
                path('', views.UserViews.user),
                # todo POST createDataType
                path('datatypes', views.UserViews.data_types),
                # todo GET getDataFields, POST createDataField
                # path('datafields/', views.getUserDataFields),
                path('posts/', views.UserViews.posts)
                # todo GET lastVotedByUser
                # path('votes/', views.getUserVotes)
            ])),
        ])),
        # todo post related views
        path('p/', include([
            path('', views.PostViews.index),
            path('<url>/', include([
                # todo GET getPost, PATCH updatePost, DELETE deletePost
                # path('', views.Post),
                # todo POST vote, PATCH updateVote, DELETE deleteVote
                # path('vote', views.Vote),
            ]))
        ])),
        # todo wikidata related views
        # path('wiki', views.wiki)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    # todo https://docs.djangoproject.com/en/2.2/howto/static-files/ it is not suitable on prod

