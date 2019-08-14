from django.contrib import admin
from .models import User, Task, LearningPath, TaskSubmission

# Register your models here.
admin.site.register(User)
admin.site.register(Task)
admin.site.register(LearningPath)
admin.site.register(TaskSubmission)