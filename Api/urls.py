from django.urls import path
from .views import (
    MenteerRegistrationAPIView, MentorRegistrationAPIView, LoginAPIView, TaskList, TaskDetail, 
        LearningPathList, LearningPathDetail
)

app_name = 'api'

urlpatterns = [
    path('registration/mentor', MentorRegistrationAPIView.as_view()),
    path('registration/mentee', MenteerRegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
    path('paths', LearningPathList.as_view()),
    path('paths/<int:pk>', LearningPathDetail.as_view()),
]
