# equilibreapp/cadastro/views.py

from django.shortcuts import render

def home(request):
    return render(request,'cadastro/home.html')