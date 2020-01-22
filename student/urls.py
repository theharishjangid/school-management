from django.urls import path
from .views import (StudentList, StudentDetail, ClassRoomList, ClassRoomDetail, StaffList, StaffDetail,
                    SubjectList, SubjectDetail, MarksList, MarksDetail)

urlpatterns = [
    path('student/', StudentList.as_view()),
    path('student/<int:pk>/', StudentDetail.as_view()),
    path('classroom/', ClassRoomList.as_view()),
    path('classroom/<int:pk>/', ClassRoomDetail.as_view()),
    path('staff/', StaffList.as_view()),
    path('staff/<int:pk>/', StaffDetail.as_view()),
    path('subject/', SubjectList.as_view()),
    path('subject/<int:pk>/', SubjectDetail.as_view()),
    path('marks/', MarksList.as_view()),
    path('marks/<int:pk>/', MarksDetail.as_view()),
]