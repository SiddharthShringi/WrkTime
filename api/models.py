from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True



class LearningPath(BaseModel):
    title = models.CharField(max_length=100)
    tasks = models.ManyToManyField(Task)
    students = models.ManyToManyField(User,  related_name='learning_paths')



class Task(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    submission = models.CharField(max_length=200)
    feedback = models.TextField()
    is_submitted = models.BooleanField(default=False)
    is_reviewed = models.BooleanField(default=False)