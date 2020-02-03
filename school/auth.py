from rest_framework import permissions
from django.contrib.auth.models import Group

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsStudentReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if (Group.objects.get(name='student').user_set.filter(id=request.user.id).exists() and
                request.method in SAFE_METHODS):
            return True
        elif Group.objects.get(name='teacher').user_set.filter(id=request.user.id).exists():
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False


class IsTeacherReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if (Group.objects.get(name='teacher').user_set.filter(
                id=request.user.id).exists() and request.method in SAFE_METHODS):
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if (Group.objects.get(name='student').user_set.filter(
                id=request.user.id).exists() and request.method in SAFE_METHODS):
            return True
        elif (Group.objects.get(name='teacher').user_set.filter(
                id=request.user.id).exists() and request.method in SAFE_METHODS):
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False
