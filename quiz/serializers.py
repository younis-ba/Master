from rest_framework import serializers
import os 

from quiz.models import Practice, QuestionChoice,QuestionMatch,QuestionPractice,InstructionExam

class InstructionExamSerializers(serializers.ModelSerializer):
    class Meta:
        model=InstructionExam
        fields="__all__"


class QuestionPracticeSerializers(serializers.ModelSerializer):
    class Meta:
        model=QuestionPractice
        fields=('text_question','text_to_voice')

class QuestionMatchSerializers(serializers.ModelSerializer):
    class Meta:
        model=QuestionMatch
        fields="__all__"

class QuestionChoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model=QuestionChoice
        fields="__all__"

class QuestionChoicePracticeSerializers(serializers.ModelSerializer):
    class Meta:
        model=QuestionChoice
        fields="__all__"


class PracticeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Practice
        fields=("q_choice","q_match","q_practice")
        depth=1