from django.contrib import admin
from .models import Question, QuestionChoice, Subject, UserQuizResult

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active', )
    list_display_links = ('name', )

@admin.register(UserQuizResult)
class  UserQuizResultAdmin(admin.ModelAdmin):
    list_display = (
        'quantity_right_answer', 'quantity_wrong_answer', 
        'quiz_result', 'author','subject'
        )
    list_display_links = ('quiz_result', )

class QuestionChoiceInLine(admin.StackedInline):
    model = QuestionChoice

@admin.register(Question)
class QuestionsAdmin(admin.ModelAdmin):
    inlines = [QuestionChoiceInLine]
