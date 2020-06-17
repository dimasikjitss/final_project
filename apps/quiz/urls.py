from django.urls import path
from .views import QuizViewList, QuizDetailView

urlpatterns = [
    path('', QuizViewList.as_view(), name='quiz_list'),
    path('<int:pk>/', QuizDetailView.as_view(), name='quiz_detail'),
]
