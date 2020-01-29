from rest_framework import permissions
from django.contrib.auth.models import Group

class IsStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        if Group.objects.get(name='student').user_set.filter(id=request.user.id).exists():
            return True
        else:
            return False


class IsTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        if Group.objects.get(name='teacher').user_set.filter(id=request.user.id).exists():
            return True
        else:
            return False
