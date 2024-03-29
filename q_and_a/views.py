from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from rest_framework import permissions

from .models import Question, Answer, Subject, QuestionImage
from .serializers import (
	QuestionSerializer,
	AnswerSerializer,
	SubjectSerializer,
	QuestionImageSerializer,
)

class QuestionViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.AllowAny,)
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

	def get_permissions(self):
		if self.action == 'create':
			return [permissions.IsAuthenticated(), ]

		return super().get_permissions()

class AnswerViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.AllowAny,)
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer


	def get_permissions(self):
		if self.action == 'create':
			return [permissions.IsAuthenticated(), ]

		return super().get_permissions()

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