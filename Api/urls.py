from django.urls import path
from .views import (
    MenteerRegistrationAPIView, MentorRegistrationAPIView, LoginAPIView
)

app_name = 'api'

urlpatterns = [
    path('registration/mentor', MentorRegistrationAPIView.as_view()),
    path('registration/mentee/', MenteerRegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]