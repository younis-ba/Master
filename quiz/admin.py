from django.contrib import admin
from quiz.models import (QuestionChoice ,QuestionPractice,QuestionMatch,
                        InstructionExam,Practice)
# Register your models here.

class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display=['departmant','lesson','question','op1','op2','op3','op4','ans']

class PracticeAdmin(admin.ModelAdmin):
    list_display=['lesson','q_choice','q_match','q_practice']


class QuestionPracticeAdmin(admin.ModelAdmin):
    list_display=['text_question','text_to_voice','ans_1','ans_2']

class QuestionMatchAdmin(admin.ModelAdmin):
    list_display=['audio','text_to_voice']

class InstructionExamAdmin(admin.ModelAdmin):
    list_display=['departmant','instruction']


admin.site.register(InstructionExam,InstructionExamAdmin)
admin.site.register(QuestionChoice,QuestionChoiceAdmin)
admin.site.register(Practice,PracticeAdmin)
admin.site.register(QuestionPractice,QuestionPracticeAdmin)
admin.site.register(QuestionMatch,QuestionMatchAdmin)