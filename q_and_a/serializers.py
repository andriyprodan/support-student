from rest_framework import serializers

from .models import Question, Answer, Subject, QuestionImage, Image
from users.serializers import UserSerializer

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'content', 'author', ]

class QuestionSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    subject = serializers.SlugRelatedField(read_only=True, slug_field="name")
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'content', 'points', 'subject', 'answers', 'author',]

class QuestionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionImage
        fields = ['id', 'image']