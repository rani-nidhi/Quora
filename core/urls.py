from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('post-question/', views.post_question, name='post_question'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('like-answer/<int:answer_id>/', views.like_answer, name='like_answer'),
]
