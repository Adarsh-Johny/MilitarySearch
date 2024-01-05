from rest_framework import serializers
from django.contrib.auth.models import User

#Map json objects to db entries
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email']