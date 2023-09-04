from django.contrib.auth.models import User, Group
from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    value = serializers.CharField(max_length=200)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class LoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    surname = serializers.CharField(max_length=200)
    login = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    avatar = serializers.CharField(max_length=200)
    password = serializers.CharField(
        write_only=True)  # write_only=True означає, що поле password не повертається відповіддю


class RegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    surname = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    avatar = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)
    

class RegistrationResponse(serializers.Serializer):
    message = serializers.CharField()
