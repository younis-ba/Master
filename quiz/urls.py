from django.urls import path
from quiz.views import (InstructionExamList,UpdateInstructionExam, PracticeQ, UpdateQuestionChoice, WarmupQ, 
                        ExamQ, QuestionChoiceList,submit_choice_q,submit_practic_q)


urlpatterns = [
    # path('<int:id>/instruction/', Instructionexam.as_view()),

    path('<int:id>/warmup/',WarmupQ.as_view()),
    path('<int:id>/exam/',ExamQ.as_view()),
    path('<int:id>/practice/',PracticeQ.as_view()),

    path('<int:id>/exam/instruction/',InstructionExamList.as_view()),
    path('<int:pk>/exam/instruction-update/',UpdateInstructionExam.as_view()),

    path('<int:id>/choice/',QuestionChoiceList.as_view()),
    path('<int:pk>/choice-update/',UpdateQuestionChoice.as_view()),


    path('<int:id>/submit-choice/',submit_choice_q),
    path('<int:id>/submit-practice/',submit_practic_q),

]
