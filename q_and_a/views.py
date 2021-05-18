from django.shortcuts import render
from rest_framework import viewsets

from .models import Question, Answer, Subject
from .serializers import (
	QuestionSerializer,
	AnswerSerializer,
	SubjectSerializer,
)

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer

class SubjectViewSet(viewsets.ModelViewSet):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
