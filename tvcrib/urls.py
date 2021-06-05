from django.urls import path
from . import views

app_name = 'tvcrib'
urlpatterns = [
    path('', views.home),
]
