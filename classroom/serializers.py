from .models import ClassRoom, ClassRoomStaffMapping, StudentClassRoomMapping
from rest_framework import serializers
from django.contrib.auth.models import User


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'


class ClassRoomStaffMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoomStaffMapping
        fields = '__all__'


class StudentClassRoomMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClassRoomMapping
        fields = '__all__'


class ClassRoomStudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, source='classroom.name')
    students = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
