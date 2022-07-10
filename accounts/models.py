from xmlrpc.client import TRANSPORT_ERROR
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from base.models import Departmant, Lesson


class User(AbstractUser):
  """
  Implement user model 
  """

  is_student = models.BooleanField(default=True)
  is_teacher = models.BooleanField(default=False)
  
  def __str__(self):
       return self.username

class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name="teacher")

    def __str__(self):
        return self.user.username


class Student(models.Model):
  """
  Implement student mode 
  """
  student = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True, related_name="student")
  age=models.IntegerField(blank=True)
  def __str__(self):
      return self.student.username

class Grade(models.Model):
  """
  Implement Grade model
  """
  student=models.ForeignKey(Student,on_delete=models.CASCADE)
  departmant=models.ForeignKey(Departmant,on_delete=models.CASCADE)
  lesson_accomplished=models.IntegerField(default=0)
  pas_exam=models.BooleanField(default=False)
  Exam_score = models.CharField(max_length=255,blank=True,null=True,verbose_name = "Student Test Score")


class ResultLesson(models.Model):
  lesson=models.ForeignKey(Student,on_delete=models.CASCADE)
  is_warmup=models.BooleanField(default=False)
  is_lesson=models.BooleanField(default=False)
  is_practice=models.BooleanField(default=False)
