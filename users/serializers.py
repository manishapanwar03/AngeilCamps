from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import PersonalToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
    def create(self, data):
        password = data.pop('password', None)
        user = super().create(data)
        if password is not None:
            user.password = make_password(password)
            user.save()
        return user
    


class PersonalTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalToken
        fields = ['id', 'token']


