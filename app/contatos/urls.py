from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # definindo a rota da página index    
]
