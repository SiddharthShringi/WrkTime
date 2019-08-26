from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .serializers import (
    MenteeRegistrationSerializer, MentorRegistrationSerializer, LoginSerializer, TaskSerializer, LearningPathSerializer
)
from .models import Task, LearningPath
from .renderers import UserJSONRenderer


# Registration Views

class MentorRegistrationAPIView(APIView):
    renderer_classes = (UserJSONRenderer,)
    serializer_class = MentorRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        print(request.data, 'data')
        user = request.data.get('user', {})
        print(user, 'user')
        serializer = self.serializer_class(data=user)
        print(serializer.is_valid(), 'is_valid')
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MenteerRegistrationAPIView(APIView):
    renderer_classes = (UserJSONRenderer,)
    serializer_class = MenteeRegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Login view for both mentor and mentee
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        print(user, 'login_user')

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# Create and read the list of the tasks.
class TaskList(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self, request):
        tasks = self.queryset.all()
        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(mentor=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# get a task object, update and delete view.
class TaskDetail(APIView):
    "Retrieve, Update and Delete instance."
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = self.serializer_class(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        task = Task.objects.get(pk=pk)
        serializer = self.serializer_class(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(mentor=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Get the list of all learning paths and create one learning path.
class LearningPathList(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LearningPathSerializer

    def get(self, request):
        paths = LearningPath.objects.all()
        serializer = self.serializer_class(paths, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(mentor=request.user)
        return Response(serializer.data, status=status.HTTP_201_OK)


# Get the learning path object, update or delete view.
class LearningPathDetail(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LearningPathSerializer

    def get_object(self, pk):
        try:
            return LearningPath.objects.get(pk=pk)
        except LearningPath.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        path = self.get_object(pk)
        serializer = self.serializer_class(path)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        path = self.get_object(pk)
        serializer = self.serializer_class(path, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(mentor=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        path = self.get_object(pk)
        path.delete()
        return Response(status=status.HTTP_204_OK)




