from django.urls import path
from . import views

app_name = 'contactos'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('add/', views.add, name='add'),
    path('remove/<int:contacto_id>', views.remove, name='remove'),
    path('edit/<int:contacto_id>', views.edit, name='edit'),
]
