from django.urls import path
from . import views

app_name = 'quizz'

urlpatterns = [
    path('', views.quizz, name='quizz'),
]
