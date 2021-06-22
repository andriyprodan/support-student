from rest_framework import serializers
from django.contrib.auth.models import User

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
            raise serializers.ValidationError("User with this id does not exists")
        return value
    
    def create(self, validated_data):
        print(validated_data)
        author_id = validated_data.pop('author_id')
        author = User.objects.get(pk=author_id)
        subject_id = 1
        subject = Subject.objects.get(pk=subject_id)
        instanse = self.Meta.model(author=author, subject=subject, **validated_data)
        instanse.save()
        return instanse

class QuestionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionImage
        fields = ['id', 'image']