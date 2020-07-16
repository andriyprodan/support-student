from django.shortcuts import render
from django.views.generic import ListView

from .models import Question

class QuestionListView(ListView):
	model = Question
	template_name = 'q_and_a/home.html'
	context_object_name = 'questions'

 