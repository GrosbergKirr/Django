from django.shortcuts import render, redirect

from django.http import HttpResponse
from random import *
from string import *
from .forms import LinksForm
from .models import Links
from django.db import connection

def index(request):
    return HttpResponse('<h4>main page<h4>')


def url_gen():
    return ''.join(choice(ascii_lowercase+ascii_uppercase)
                   for _ in range(randint(6,12)))

def create(request):

    if request.method == "POST":
        form = LinksForm(request.POST)
        url = request.POST.get('url')  # ПОЛУЧЕНИЕ ДАННЫХ ИЗ ФОРМЫ
        alias = request.POST.get('alias')
        try:
            a = Links.objects.get(url=url).alias
            return HttpResponse(f'Такая ссылка уже есть. Ее алиас: {a}',)
        except Links.DoesNotExist:
            try:
                b = Links.objects.get(alias=alias).url
                return HttpResponse(f'Такой алиас уже есть. Его ссылка: {b}',)
            except Links.DoesNotExist:
                # -----------Save to bd----------
                if form.is_valid():
                    form.save()
            return HttpResponse('Все четко все сохранилось!')



    form1 = LinksForm

    data = {
        'form1': form1,
        'error': error
    }
    return render(request,'main/create.html', data)

def geturl(request):
    error = ''
    if request.method == 'POST':
        alias = request.POST.get('alias') # ПОЛУЧЕНИЕ ДАННЫХ ИЗ ФОРМЫ

        # a = Links.objects.filter(alias=alias).first().url
        try:
            a = Links.objects.get(alias=alias).url
            return HttpResponse(a)
        except Links.DoesNotExist:
            return HttpResponse('Нет ссылки с таким алиасом')
    else:
        error = 'Неверный алиас'

    form2 = LinksForm

    data = {
        'form2': form2,
        'error': error,
    }
    return render(request,'main/geturl.html', data)



def response(request, row):

    return render(request, 'main/response.html',)