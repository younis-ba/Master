from rest_framework import viewsets
from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from .models import User
from .serializers import StudentCustomRegistrationSerializer, TeacherCustomRegistrationSerializer



class StudentRegistrationView(RegisterView):
    serializer_class = StudentCustomRegistrationSerializer


class TeacherRegistrationView(RegisterView):
    serializer_class = TeacherCustomRegistrationSerializer