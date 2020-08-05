from django.urls import path

from .views import (
	QuestionCreateView,
	QuestionListView,
	QuestionDetail,
)

app_name = 'q_and_a'
urlpatterns = [
    path('', QuestionListView.as_view(), name='home'),
    path('ask/', QuestionCreateView.as_view(), name='ask'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='question-detail'),
    
]