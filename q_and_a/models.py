from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
	title = models.CharField(max_length=127)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Answer(models.Model):
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __str__(self):
		return f'Question: {self.question.title} | ' + self.content