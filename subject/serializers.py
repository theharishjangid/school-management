from .models import Subject, SubjectStaffMapping, Marks
from rest_framework.serializers import ModelSerializer


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class SubjectStaffMappingSerializer(ModelSerializer):
    class Meta:
        model = SubjectStaffMapping
        fields = '__all__'


class MarksSerializer(ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'
