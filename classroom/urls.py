from django.urls import path
from .views import (ClassRoomList, ClassRoomDetail, ClassRoomStaffMappingList, ClassRoomStaffMappingDetail,
                    StudentClassRoomMappingList, StudentClassRoomMappingDetail, ClassRoomStudent,
                    ClassRoomStudentDetail)

urlpatterns = [
    path('classroom/', ClassRoomList.as_view()),
    path('classroom/<int:pk>/', ClassRoomDetail.as_view()),
    path('classroomstaff/', ClassRoomStaffMappingList.as_view()),
    path('classroomstaff/<int:pk>/', ClassRoomStaffMappingDetail.as_view()),
    path('studentclass/', StudentClassRoomMappingList.as_view()),
    path('studentclass/<int:pk>/', StudentClassRoomMappingDetail.as_view()),
    path('classstudent/', ClassRoomStudent.as_view()),
    path('classstudent/<int:pk>/', ClassRoomStudentDetail.as_view()),
]