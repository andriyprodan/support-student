from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from . import views

router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)

app_name = 'q_and_a'
urlpatterns = [
    path('upload_question_image/', views.UploadQuestionImageView.as_view(), name='upload_question_image'),
    path('subjects/', views.SubjectList.as_view(), name='get_subjects'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls