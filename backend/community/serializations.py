from .models import *
from rest_framework import serializers


class MembershipSerializer(serializers.ModelSerializer):
    community = serializers.StringRelatedField()

    class Meta:
        model = Membership
        fields = [
            'community',
            'role',
            'date_joined'
        ]


class UserSerializer(serializers.ModelSerializer):
    communities = MembershipSerializer(many=True)
    posts = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = '__all__'


class CommunitySerializer(serializers.ModelSerializer):
    pass

