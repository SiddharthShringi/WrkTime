from django.urls import path
from .views import (
    MenteerRegistrationAPIView, MentorRegistrationAPIView, LoginAPIView, TaskAPIView
)

app_name = 'api'

urlpatterns = [
    path('registration/mentor', MentorRegistrationAPIView.as_view()),
    path('registration/mentee/', MenteerRegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('tasks/', TaskAPIView.as_view()),
]