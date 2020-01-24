from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'date_of_birth', 'phone_no', 'first_name', 'last_name')

class StudentSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(source='userprofile.date_of_birth')
    phone_no = serializers.IntegerField(source='userprofile.phone_no')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'date_of_birth', 'phone_no',]