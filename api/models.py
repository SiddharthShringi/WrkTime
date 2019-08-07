import jwt
from datatime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if email is None:
            raise TypeError('User must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_mentor(self, email, password, **extra_fields):
        if password is None:
            raise TypeError('User must have password.')

        user = self.create_user(email, password, **extra_fields)
        user.is_mentor = True
        user.save()

        return user

    def create_student(self, email, password, **extra_fields):
        if password is None:
            raise TypeError('User must have password.')

        user = self.create_user(email, password, **extra_fields)
        user.is_student = True
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        if password is None:
            raise TypeError('User must have password')

        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_mentor = models.BooleanField(default=False)
    is_student = models.BooleanField(defult=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = ('users')

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        first_name_initial = self.first_name[0].upper()
        last_name_initial = self.last_name[0].upper()
        return first_name_initial+last_name_initial

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datatime.now() + timedelta(days=30)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def __str__(self):
        return self.full_name()


class Task(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')

    def __str__(self):
        return self.name


class LearningPath(BaseModel):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('learning path')
        verbose_name_plural = _('learning paths')

    def __str__(self):
        return self.title


class TaskSubmission(BaseModel):
    learning_path = models.ForeignKey(
        LearningPath, on_delete=models.CASCADE, related_name='submissions')
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    due_date = models.DateField()
    submission = models.CharField(max_length=100)
    feedback = models.TextField()
    priority = models.IntegerField()
    is_submitted = models.BooleanField(default=False)
    is_reviewed = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Task Submission')

    def __str__(self):
        return self.task_id
