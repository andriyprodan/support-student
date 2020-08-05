from django.shortcuts import render
from django.views import View
from django.views.generic import (
	ListView,
	DetailView,
	CreateView
)
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Question, Subject, Answer
from .forms import QuestionCreateForm, AnswerCreateForm

class QuestionCreateView(LoginRequiredMixin, CreateView):
	model = Question
	form_class = QuestionCreateForm
	success_url = reverse_lazy('q_and_a:home')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		# Prevent the user from giving more points for the right answer than he/she has
		kwargs.update({'user_points': self.request.user.profile.points})
		return kwargs


class QuestionListView(ListView):
	model = Question
	template_name = 'q_and_a/home.html'
	context_object_name = 'questions'


class QuestionDisplay(DetailView):
	model = Question

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# place the answer creation form at the question detail view
		context['answer_form'] = AnswerCreateForm()
		return context

class AnswerCreateView(CreateView):
	model = Answer
	form_class = AnswerCreateForm
	template_name = 'q_and_a/question_detail.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.question = Question.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)
	
	def get_success_url(self):
		return reverse_lazy('q_and_a:question-detail', kwargs={'pk': self.object.question_id})

class QuestionDetail(View):

	def get(self, request, *args, **kwargs):
		view = QuestionDisplay.as_view()
		return view(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		view = AnswerCreateView.as_view()
		return view(request, *args, **kwargs)
