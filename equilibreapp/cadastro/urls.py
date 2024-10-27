from django.urls import path
from . import views

app_name = 'cadastro'

urlpatterns = [
    path('', views.home, name='home'),
]

