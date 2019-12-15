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
                path('datatypes/', views.CommunityViews.data_types),
                path('posts/', views.CommunityViews.posts)
            ]))
        ])),
        # todo user related views
        path('u/', include([
            path('', views.UserViews.index),
            # todo GET loginform?, POST login
            path('login', views.UserViews.login),
            path('logout', views.UserViews.logout),
            # todo GET signupform?, POST signup
            # path('signup', views.Signup),
            path('<username>/', include([
                path('', views.UserViews.user),
                path('datatypes/', views.UserViews.data_types),
                path('datatype/<id>', views.UserViews.data_type),
                path('posts/', views.UserViews.posts),
                path('votes/', views.UserViews.votes)
            ])),
        ])),
        # todo post related views
        path('p/', include([
            path('', views.PostViews.index),
            # todo POST create
            # path('new', views.PostViews.create),
            path('<url>/', include([
                path('', views.PostViews.post),
                path('vote', views.PostViews.vote),
            ]))
        ])),
        # todo wikidata related views
        # path('wiki', views.wiki)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    # todo https://docs.djangoproject.com/en/2.2/howto/static-files/ it is not suitable on prod

