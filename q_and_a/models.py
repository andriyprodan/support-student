from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class Subject(models.Model):
	name = models.CharField(max_length=127, unique=True)

	def __str__(self):
		return self.name

class Question(models.Model):
	title = models.CharField(max_length = 127, verbose_name= _("Question title"))
	content = models.TextField(verbose_name= _("Question content"))
	points = models.PositiveIntegerField(
		default = 0,
		verbose_name = _("Points for correct answer"),
	)
	date_posted = models.DateTimeField(default = timezone.now)

	author = models.ForeignKey(User, on_delete = models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
	correct_answer_id = models.PositiveIntegerField()

	def __str__(self):
		return self.title

class Answer(models.Model):
	content = models.TextField()
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	question = models.ForeignKey(Question, related_name="answers", on_delete = models.CASCADE)

	def __str__(self):
		return f'Answer to the question: {self.question.title} | {self.content}'