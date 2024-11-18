from django.urls import path
from .views import UserListView, QuestionList, FacultyList, AnswerList 

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('questions/', QuestionList.as_view(), name='question-list'),
    path('questions/<int:question_id>/answers/', AnswerList.as_view(), name='question-list'),


    # path('answers/', AnswerList.as_view(), name='answer-list'),
    path('faculties/', FacultyList.as_view(), name='faculty-list')]
