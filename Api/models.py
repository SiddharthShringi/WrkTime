import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if email is None:
            raise TypeError('User must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        if password is None:
            raise TypeError('Superusers must have password.')

        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    def create_mentor(self, email, password, **extra_fields):
        if password is None:
            raise TypeError('User must have password.')

        user = self.create_user(email, password, **extra_fields)
        user.is_mentor = True
        user.save()

        return user

    def create_mentee(self, email, password, **extra_fields):
        if password is None:
            raise TypeError('User must have password.')

        user = self.create_user(email, password, **extra_fields)
        user.is_mentee = True
        user.save()

        return user


class User(AbstractBaseUser, TimeStampModel, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_mentor = models.BooleanField(default=False)
    is_mentee = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):

        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        # first_name_initial = self.first_name[0].upper()
        # last_name_initial = self.last_name[0].upper()
        # return first_name_initial+last_name_initial
        return self.first_name

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LearningPath(models.Model):
    title = models.CharField(max_length=30)
    mentee = models.OneToOneField(User, on_delete=models.CASCADE)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paths')
    
    def __str__(self):
        return self.title


class TaskSubmission(models.Model):
    path = models.ForeignKey(
        LearningPath, on_delete=models.CASCADE, related_name='task_submissions')
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    submission = models.CharField(max_length=100, blank=True)
    feedback = models.TextField(blank=True)
    is_submitted = models.BooleanField(default=False)
    is_reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_id.name


# to do task
# 1. Make user serializer
# 2. Write views for accessing users who are mentee.


# Serializer



