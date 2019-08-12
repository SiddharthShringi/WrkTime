from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MenteeRegistrationSerializer, MentorRegistrationSerializer


# Registration Views

class MentorRegistrationAPIView(APIView):
    serializer_class = MentorRegistrationSerializer


    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MeneerRegistrationAPIView(APIView):
    serializer_class = MenteeRegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)



