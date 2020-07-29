from django import forms
from .models import Question, Answer
from django.core.validators import MaxValueValidator

class QuestionCreateForm(forms.ModelForm):

	class Meta:
		model = Question
		fields = ['title', 'content', 'subject', 'points']	

	def __init__(self, *args, **kwargs):
		user_points = kwargs.pop('user_points', None)
		super().__init__(*args, **kwargs)
		self.fields['points'].widget.attrs.update({'max': user_points})