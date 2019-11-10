from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login),
    path('c/<int:community_id>', views.getCommunity)
]