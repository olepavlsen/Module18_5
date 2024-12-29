from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def site_main(request):
    title = 'Игровая платформа'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'platform.html', context)


def shop(request):
    title = 'Магазин'
    text = 'Игры'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'games.html', context)


def basket(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'cart.html', context)
