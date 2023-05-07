from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)


def cycle(request):
    data = {
        'title': 'Перемножение циклов'
    }
    return render(request, 'main/cycle.html', data)