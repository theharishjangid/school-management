from django.urls import path
from .views import UserProfileList, UserProfileDetail, StudentList, StudentDetail, StaffList, StaffDetail

urlpatterns = [
    path('user/', UserProfileList.as_view()),
    path('user/<int:pk>/', UserProfileDetail.as_view()),
    path('student/', StudentList.as_view()),
    path('student/<int:pk>/', StudentDetail.as_view()),
    path('staff/', StaffList.as_view()),
    path('staff/<int:pk>/', StaffDetail.as_view()),

]