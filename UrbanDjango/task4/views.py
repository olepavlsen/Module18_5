from django.shortcuts import render


# Create your views here.

def site_main(request):
    title = 'Главная страница'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'platform.html', context)


def shop(request):
    title = 'Игры'
    text = 'Игры'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'title': title,
        'text': text,
        'list': games,
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
