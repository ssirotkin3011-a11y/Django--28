from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime
import os


def home_view(request):
    pages = [
        '/',
        '/current_time/',
        '/workdir/',
    ]

    context = {
        'pages': pages
    }

    return render(request, 'index.html', context)


def current_time_view(request):
    current_time = datetime.now()

    return HttpResponse(f'Текущее время: {current_time}')


def workdir_view(request):
    files = os.listdir('.')

    return HttpResponse('<br>'.join(files))