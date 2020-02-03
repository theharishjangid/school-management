from django.urls import path
from .views import (SubjectList, SubjectDetail, SubjectStaffMappingList, SubjectStaffMappingDetail, MarksList,
                    MarksDetail)

urlpatterns = [
    path('subject/', SubjectList.as_view()),
    path('subject/<int:pk>/', SubjectDetail.as_view()),
    path('subjectstaff/', SubjectStaffMappingList.as_view()),
    path('subjectstaff/<int:pk>/', SubjectStaffMappingDetail.as_view()),
    path('marks/', MarksList.as_view()),
    path('marks/<int:pk>/', MarksDetail.as_view()),
]