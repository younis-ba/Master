from rest_framework.routers import DefaultRouter
from accounts.views import StudentRegistrationView, TeacherRegistrationView
from django.urls import path,include


# The API URLs are now determined automatically by the router.
urlpatterns = [
    #Registration Urls
    path('registration/student/', StudentRegistrationView.as_view(), name='register-student'),
    path('registration/teacher/', TeacherRegistrationView.as_view(), name='register-teacher'),
    
]