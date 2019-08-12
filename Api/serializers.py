from django.contrib.auth import authenticate
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



class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('An email address is required to login.')

        if password is None:
            raise serializers.ValidationError('A password is required to login.')


        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this email and password does not exist.')

        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated.')

        return {
            'email': user.email,
            'password': user.password,
            'token': user.token
        }



    
