from django.urls import path
from . import views

app_name = 'diagnostico'

urlpatterns = [
    path('', views.index, name='index'),
    path('realizar_predicao/', views.realizar_predicao, name='realizar_predicao'),
]
