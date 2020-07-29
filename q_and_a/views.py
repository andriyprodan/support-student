from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Question, Subject
from .forms import QuestionCreateForm, AnswerCreateForm
from .mixins import AjaxableResponseMixin

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

class QuestionDetailView(DetailView):
	model = Question
	form_class = AnswerCreateForm

class AnswerCreateView(AjaxableResponseMixin, LoginRequiredMixin, CreateView):
	model = Answer
	fields = ['content']

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response
