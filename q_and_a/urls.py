from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)
router.register(r'subjects', views.SubjectViewSet)

app_name = 'q_and_a'
urlpatterns = [

]

urlpatterns += router.urls