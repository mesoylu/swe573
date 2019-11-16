from django.urls import path, include

from . import views

urlpatterns = [
    path('login', views.login),
    path('c/<url>/', include([
        path('', views.getCommunity),
        path('members/', views.getCommunityMembers),
        path('datatypes/', views.getCommunityDataTypes),
        path('datafields/', views.getCommunityDataFields),
        path('posts/', views.getCommunityPosts),
    ])
    ),
    path('wiki', views.wiki),
    path('wikiItem', views.wikiItem)
]


