from django.urls import path
from .views import ClassRoomList, ClassRoomDetail, ClassRoomStaffMappingList, ClassRoomStaffMappingDetail

urlpatterns = [
    path('classroom/', ClassRoomList.as_view()),
    path('classroom/<int:pk>/', ClassRoomDetail.as_view()),
    path('classroomstaff/', ClassRoomStaffMappingList.as_view()),
    path('classroomstaff/<int:pk>/', ClassRoomStaffMappingDetail.as_view()),
]