from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .models import Question, Answer, Subject, QuestionImage
from .serializers import (
	QuestionSerializer,
	AnswerSerializer,
	SubjectSerializer,
	QuestionImageSerializer,
)

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			print(serializer.data)
			return Response(serializer.data, status=status.HTTP_201_CREATED)

class AnswerViewSet(viewsets.ModelViewSet):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer

class SubjectList(ListAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer

class UploadQuestionImageView(APIView):
	def post(self, request, format=None):
		serializer = QuestionImageSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			# kriven'ko
			if request.META['SERVER_PROTOCOL'] == 'HTTP/1.1':
				protocol = 'http://'
			url = protocol + request.META['HTTP_HOST'] + '/api' + settings.MEDIA_URL + str(serializer.instance.image)
			return Response({'id': serializer.instance.id, 'url': url}, status=status.HTTP_200_OK)
		return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)