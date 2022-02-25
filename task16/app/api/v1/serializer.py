from django.contrib.auth.models import User
from app.models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'first_name', 'last_name',
                  'username', 'email', 'reign_name']

# class ProfileSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = "__all__"
