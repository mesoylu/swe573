from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

# todo https://docs.djangoproject.com/en/2.2/howto/static-files/ it is not suitable on prod
urlpatterns = [
    path('login', views.login),
    path('c/<name>/', include([
        path('', views.getCommunity),
        path('members/', views.getCommunityMembers),
        path('datatypes/', views.getCommunityDataTypes),
        path('datafields/', views.getCommunityDataFields),
        path('posts/', views.getCommunityPosts),
    ])
    ),
    path('u/<username>/', include([
        path('', views.getUser),
    ])),
    path('wiki', views.wiki)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


