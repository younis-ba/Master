
from django.db import models
from base.models import Lesson,Departmant
# Create your models here.

class QuestionChoice(models.Model):
    departmant=models.ForeignKey(Departmant,on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE,related_name="lesson_C")
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True,blank=True)
    op2 = models.CharField(max_length=200,null=True,blank=True)
    op3 = models.CharField(max_length=200,null=True,blank=True)
    op4 = models.CharField(max_length=200,null=True,blank=True)
    ans = models.CharField(max_length=200,null=True,blank=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.question

class QuestionPractice(models.Model):
    text_question=models.TextField(blank=True,null=True)
    text_to_voice =models.FileField(upload_to='audio/', null=True)
    ans_1 = models.CharField(max_length=200,null=True,blank=True)
    ans_2 = models.CharField(max_length=200,null=True,blank=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.text_question

class QuestionMatch(models.Model):
    audio =models.FileField(upload_to='audio/', null=True)
    text_to_voice=models.TextField(blank=True,null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.text_to_voice

class Practice(models.Model):
    lesson=models.OneToOneField(Lesson,on_delete=models.CASCADE)
    q_choice=models.OneToOneField(QuestionChoice, on_delete=models.CASCADE)
    q_match=models.OneToOneField(QuestionMatch, on_delete=models.CASCADE)
    q_practice=models.OneToOneField(QuestionPractice, on_delete=models.CASCADE)
    def __str__(self):
        return self.lesson.title

class InstructionExam(models.Model):
    """
    Implement Instruction models 
    """
    departmant              =models.ForeignKey(Departmant,on_delete=models.CASCADE , related_name='instruction_exam')
    instruction             =models.TextField(blank=True,null=True)

    def __str__(self):
        return self.instruction 