from rest_framework import serializers
from .models import User



class MentorRegistrationSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    # Client should not be able to send token along with the registratino
    # request. So to ensure that we are making token read_only.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'token']

    
    def create(self, validated_data):
        return User.objects.create_mentor(**validated_data)


class MenteeRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    # Client should not be able to send token along with the registratino
    # request. So to ensure that we are making token read_only.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'token']

    
    def create(self, validated_data):
        return User.objects.create_mentee(**validated_data)
    
