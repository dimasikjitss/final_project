from django.shortcuts import render, get_object_or_404
from .models import QuestionChoice, Question, Subject, UserQuizResult
from django.views.generic import ListView
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

class QuizViewList(ListView):
    template_name = 'quiz/quiz_list.html'
    model = Subject


class QuizDetailView(LoginRequiredMixin, View):
    template_name = 'quiz/quiz_detail.html' 
    model = Subject

    def get(self, request, pk):
        subject = get_object_or_404(self.model, pk=pk) 
        return render(request, self.template_name, locals())
   
    def post(self, request, pk):
        subject = get_object_or_404(self.model, pk=pk) 
        answers = request.POST.keys()

        #Если не чего не заполнено, но мы просто перезагружаем
        if len(answers) == 1:
            return render(request, self.template_name, locals())
        else:
            questions = Question.objects.filter(subject=subject)
            right_answers = []
            all_answers = []
            """
            Получение правильных ответов и апендим в right_answers
            all_answers это для того чтобы подсчитать процент
            """
            for answer in questions:
                for right_answer in answer.questions.filter(is_right_choice=True):
                    if right_answer not in right_answers:
                        right_answers.append(right_answer.id)
                    else:
                        continue
                all_answers.append(answer)

            count_right_answer = 0
            count_wrong_answer = 0
            for x in answers:
                try:
                    id_ = int(x)
                    if id_ in right_answers:
                        count_right_answer += 1
                    else:
                        count_wrong_answer += 1
                except:
                    continue

            #подсчет процента
            print(all_answers)
            percent_of_result = count_right_answer / len(all_answers) * 100
            print(percent_of_result)
            #Создаем объект с результатами
            user_result = UserQuizResult.objects.create(
                quantity_right_answer=count_right_answer,
                quantity_wrong_answer = count_wrong_answer,
                quiz_result = percent_of_result,
                author = request.user,
                subject = subject
            )
            
            return render(request, 'quiz/quiz_result.html', locals())

   

