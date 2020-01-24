from django.urls import path
from .views import UserProfileList, UserProfileDetail

urlpatterns = [
    path('user/', UserProfileList.as_view()),
    path('user/<int:pk>/', UserProfileDetail.as_view()),
]