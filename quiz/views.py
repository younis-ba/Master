from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from base.models import Departmant, Lesson
from quiz.serializers import (InstructionExamSerializers, QuestionChoiceSerializers,
                             QuestionMatchSerializers, QuestionPracticeSerializers,
                             QuestionChoicePracticeSerializers,PracticeSerializers)
from quiz.models import   (InstructionExam, QuestionChoice, QuestionMatch,
                            QuestionPractice,Practice)
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponse




class QuestionChoiceList(generics.ListAPIView,generics.CreateAPIView):
    serializer_class = QuestionChoiceSerializers
    def get_queryset(self):
        return QuestionChoice.objects.filter(departmant=self.kwargs['id'])



class UpdateQuestionChoice(generics.UpdateAPIView,generics.DestroyAPIView,generics.RetrieveAPIView):
    """This endpoint allows for updating a specific todo by passing 
        in the id of the todo to update"""
    
    queryset = QuestionChoice.objects.all()
    serializer_class = QuestionChoiceSerializers


class QuestionMatchList(generics.ListAPIView,generics.CreateAPIView):
    serializer_class = QuestionMatchSerializers


class UpdateQuestionMatch(generics.UpdateAPIView,generics.DestroyAPIView,generics.RetrieveAPIView):
    """This endpoint allows for updating a specific todo by passing 
        in the id of the todo to update"""
    
    queryset = QuestionMatch.objects.all()
    serializer_class = QuestionMatchSerializers


class QuestionPracticeList(generics.ListAPIView,generics.CreateAPIView):
    serializer_class = QuestionPracticeSerializers


class UpdateQuestionPractice(generics.UpdateAPIView,generics.DestroyAPIView,generics.RetrieveAPIView):
    """This endpoint allows for updating a specific todo by passing 
        in the id of the todo to update"""
    
    queryset = QuestionPractice.objects.all()
    serializer_class = QuestionPracticeSerializers


class PracticeList(generics.ListAPIView,generics.CreateAPIView):
    serializer_class = PracticeSerializers



class UpdatePractice(generics.UpdateAPIView,generics.DestroyAPIView,generics.RetrieveAPIView):
    """This endpoint allows for updating a specific todo by passing 
        in the id of the todo to update"""
    
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializers



class WarmupQ(generics.ListAPIView):
    serializer_class = QuestionChoiceSerializers

    def get_queryset(self):
        return QuestionChoice.objects.filter(lesson=self.kwargs['id'])

class PracticeQ(generics.ListAPIView):
    serializer_class = PracticeSerializers

    def get_queryset(self):
        return Practice.objects.filter(lesson=self.kwargs['id'])

class InstructionExamList(generics.ListAPIView,generics.CreateAPIView):
    serializer_class = InstructionExamSerializers

    def get_queryset(self):
        return InstructionExam.objects.filter(departmant=self.kwargs['id'])

class UpdateInstructionExam(generics.UpdateAPIView,generics.DestroyAPIView,generics.RetrieveAPIView):
    """This endpoint allows for updating a specific todo by passing 
        in the id of the todo to update"""
    
    queryset = InstructionExam.objects.all()
    serializer_class = InstructionExamSerializers

class ExamQ(generics.ListAPIView):
    serializer_class = QuestionChoiceSerializers

    def get_queryset(self):
        return QuestionChoice.objects.filter(departmant=self.kwargs['id'])





@api_view(['POST','OPTIONS'])
def submit_choice_q(request,id):
    q=QuestionChoice.objects.get(id=id)
    print(q.lesson)
    if q.ans == request.data['answer']:
        return Response({'message':'you  submit correct answer'})
    else :
        return Response({'message':'you  submit wrong answerplese review {} lesson'.format(q.lesson)})


@api_view(['POST','OPTIONS'])
def submit_practic_q(request,id):
    answer=QuestionPractice.objects.get(id=id).ans_1
    if answer == request.data['answer']:
        return Response({'message':'you  submit correct answer'})
    else :
        return Response({'message':'you  submit wrong answer'})
