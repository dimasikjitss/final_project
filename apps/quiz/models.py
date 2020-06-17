from django.db import models
from django.contrib.auth import get_user_model



class Subject(models.Model):
    """Тема, по которой идет тестирование."""
    name = models.CharField(max_length=60, verbose_name="Subject")
    description = models.CharField(max_length=255, verbose_name='Description')
    is_active = models.BooleanField(default=True, verbose_name="Active")

    def __str__(self):
        return self.name


class Question(models.Model):
    """Вопрос для  Subject"""
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')
    question_text = models.TextField(verbose_name="Question")
    is_active = models.BooleanField(default=True, verbose_name="Activity")
    is_multiple_choice = models.BooleanField(default=False)

    def __str__(self):
        return (self.question_text)


class QuestionChoice(models.Model):
    """Один из вариантов ответа для Question"""
    is_active = models.BooleanField(default=True)
    answer_text = models.TextField(verbose_name="Answer")
    is_right_choice = models.BooleanField(default=False, verbose_name="Right choice")
    parent = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.answer_text

class UserQuizResult(models.Model):
    quantity_right_answer = models.IntegerField(default=0)
    quantity_wrong_answer = models.IntegerField(default=0)
    quiz_result = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="results")
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, related_name="subjects")
    def __str__(self):
        return self.quiz_result
     
