from django.urls import path

from .views import QuestionListView

app_name = 'q_and_a'
urlpatterns = [
    path('', QuestionListView.as_view(), name='home'),
]