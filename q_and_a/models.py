from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.utils.deconstruct import deconstructible
import uuid
import os

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
	correct_answer_id = models.PositiveIntegerField(null=True)

	def __str__(self):
		return self.title

class Answer(models.Model):
	content = models.TextField()
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	question = models.ForeignKey(Question, related_name="answers", on_delete = models.CASCADE)

	def __str__(self):
		return f'Answer to the question: {self.question.title} | {self.content}'

@deconstructible
class PathAndRename(object):

		def __init__(self, sub_path):
			self.path = sub_path

		def __call__(self, instance, filename):
			ext = filename.split('.')[-1]
			# set filename as random string
			filename = f"{uuid.uuid4().hex}.{ext}"
			# return the whole path to the file
			return os.path.join(self.path, filename)

class Image(models.Model):
	image = models.ImageField(upload_to=PathAndRename("q_and_a_images/"))

class QuestionImage(Image):
	question = models.ForeignKey(Question, related_name='images', null=True, on_delete=models.CASCADE)