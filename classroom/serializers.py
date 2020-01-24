from .models import ClassRoom, ClassRoomStaffMapping
from rest_framework.serializers import ModelSerializer

class ClassRoomSerializer(ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'

class ClassRoomStaffMappingSerializer(ModelSerializer):
    class Meta:
        model = ClassRoomStaffMapping
        fields = '__all__'