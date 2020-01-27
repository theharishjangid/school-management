from .models import ClassRoom, ClassRoomStaffMapping, StudentClassRoomMapping
from rest_framework import serializers

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