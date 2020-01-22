from .models import Student, ClassRoom, Staff, Subject, Marks
from rest_framework.serializers import ModelSerializer


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ClassRoomSerializer(ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'

class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class MarksSerializer(ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'
