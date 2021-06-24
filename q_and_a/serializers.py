from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Question, Answer, Subject, QuestionImage, Image
from users.serializers import UserSerializer

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class AnswerSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField()
    question_id = serializers.IntegerField()

    class Meta:
        model = Answer
        fields = ['id', 'content', 'question_id', 'author_id', ]
        
    def validate_author_id(self, value):
        if not User.objects.filter(pk=value).exists():
            raise serializers.ValidationError("User with this id does not exists")
        return value

    def validate_question_id(self, value):
        if not Question.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Question with this id does not exists")
        return value
    
    def create(self, validated_data):
        author_id = validated_data.pop('author_id')
        author = User.objects.get(pk=author_id)
        question_id = validated_data.pop('question_id')
        question = Question.objects.get(pk=question_id)
        instanse = self.Meta.model(author=author, question=question, **validated_data)
        instanse.save()
        return instanse

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    author_id = serializers.IntegerField()
    subject_id = serializers.IntegerField()

    class Meta:
        model = Question
        fields = ['id', 'title', 'content', 'points', 'subject_id', 'author_id', 'answers', ]
        
    def validate_author_id(self, value):
        if not User.objects.filter(pk=value).exists():
            raise serializers.ValidationError("User with this id does not exists")
        return value

    def validate_subject_id(self, value):
        if not Subject.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Subject with this id does not exists")
        return value
    
    def create(self, validated_data):
        author_id = validated_data.pop('author_id')
        author = User.objects.get(pk=author_id)
        subject_id = validated_data.pop('subject_id')
        subject = Subject.objects.get(pk=subject_id)
        instanse = self.Meta.model(author=author, subject=subject, **validated_data)
        instanse.save()
        return instanse

class QuestionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionImage
        fields = ['id', 'image']