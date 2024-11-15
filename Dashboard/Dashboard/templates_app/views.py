from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Здесь 'index.html' - это твой шаблон

