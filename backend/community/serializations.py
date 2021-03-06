from .models import *
from rest_framework import serializers


class MembershipSerializer(serializers.ModelSerializer):
    community = serializers.StringRelatedField()

    class Meta:
        model = Membership
        fields = [
            'community',
            'is_admin',
            'date_joined'
        ]


class PostSerializer(serializers.ModelSerializer):
    data_type = serializers.StringRelatedField()
    community = serializers.StringRelatedField()
    creator = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    communities = MembershipSerializer(many=True)
    user_posts = PostSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'


class CommunitySerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField()
    members = serializers.StringRelatedField(many=True)
    data_types = serializers.StringRelatedField(many=True)
    community_posts = PostSerializer(many=True)

    class Meta:
        model = Community
        fields = '__all__'


class DataTypeSerializer(serializers.ModelSerializer):
    community = serializers.StringRelatedField()
    creator = serializers.StringRelatedField()

    class Meta:
        model = DataType
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Vote
        fields = '__all__'
