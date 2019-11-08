from rest_framework import serializers
from .models import *
import backend.settings.dev as settings
from rest_framework.validators import UniqueValidator
import jwt
from rest_framework_jwt.utils import jwt_payload_handler


class ProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MygUser
        fields = ['profile_pic']
        #owner = serializers.Field(source='user.username')

class MygUserSerializer(serializers.ModelSerializer):
    avatar=serializers.SerializerMethodField()
    class Meta:
        model=MygUser
        exlude=['user']
        fields=('avatar','mom','dad',)
        read_only_fields = ['profile_pic']
    def get_avatar(self,MygUser):
        request = self.context.get('request')
        try:
            IMG_url = MygUser.profile_pic.url
        except:
            IMG_url='/media/profile/e2.png'
        return IMG_url

class UserSerializer(serializers.ModelSerializer):
    myg_user = MygUserSerializer()
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','myg_user','is_staff','is_superuser','is_authenticated',]

    def create(self, validated_data):
        myg_user = validated_data.pop('myg_user')
        user = User.objects.create(**validated_data)
        MygUser.objects.create(user=user, **myg_user)
        user.set_password(user.password)
        user.save()
        return user

    def update(self, instance, validated_data):
        myg_user = validated_data.pop('myg_user')
        myg_user = instance.myg_user

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        myg_user.save()

        return instance
