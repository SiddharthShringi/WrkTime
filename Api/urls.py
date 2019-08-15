from django.urls import path
from .views import (
    MenteerRegistrationAPIView, MentorRegistrationAPIView, LoginAPIView, TaskList, TaskDetail
)

app_name = 'api'

urlpatterns = [
    path('registration/mentor', MentorRegistrationAPIView.as_view()),
    path('registration/mentee/', MenteerRegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('tasks/', TaskList.as_view()),
    path('task/<int:pk>/', TaskDetail.as_view()),
]