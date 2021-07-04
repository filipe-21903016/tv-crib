from django.urls import path
from . import views

app_name = 'tvcrib'
urlpatterns = [
    path('', views.home, name="home"),
    path('<int:show_id>', views.show, name="show"),
    path('about/', views.about, name="about"),
    path('movies/', views.all_movies, name="movies"),
    path('series/', views.all_series, name='series'),
    path('comentarios/', views.comentarios, name='comentarios'),
]
