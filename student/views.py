import logging
from .models import UserProfile
from .serializers import UserProfileSerializer, StudentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group, User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from school.auth import IsStudentReadOnly, IsTeacherReadOnly

logger = logging.getLogger(__name__)


def is_in_group(user, group_name):
    if Group.objects.get(name=group_name).user_set.filter(id=user.id).exists():
        return True
    else:
        return False


class UserProfileList(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get(self, response):
        users = UserProfile.objects.select_related('user').all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, response):
        serializer = UserProfileSerializer(data=response.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileDetail(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_object(self, pk):
        try:
            return UserProfile.objects.select_related('user').get(pk=pk)
        except UserProfile.DoesNotExist:
            logger.error("item not found")
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentList(APIView):
    permission_classes = [IsStudentReadOnly, IsAuthenticated]

    def get(self, request):
        student = [user for user in User.objects.all() if is_in_group(user, 'student')]
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StaffList(APIView):
    permission_classes = [IsTeacherReadOnly, IsAuthenticated]

    def get(self, request):
        staff = [user for user in User.objects.all() if is_in_group(user, 'teacher')]
        serializer = StudentSerializer(staff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentDetail(APIView):
    permission_classes = [IsStudentReadOnly, IsAuthenticated]

    def get_object(self, pk):
        try:
            student = User.objects.get(pk=pk)
            if is_in_group(student, 'student'):
                return student
        except User.DoesNotExist:
            logger.error("item not found")
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = StudentSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = StudentSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StaffDetail(APIView):
    permission_classes = [IsTeacherReadOnly, IsAuthenticated]

    def get_object(self, pk):
        try:
            teacher = User.objects.get(pk=pk)
            if is_in_group(teacher, 'teacher'):
                return teacher
        except User.DoesNotExist:
            logger.error("item not found")
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = StudentSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = StudentSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
