from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.

def sign_up_by_html(request):
    users = ['truelogin', 'Vasya', 'Peter', 'Ole']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        for user in users:
            if user == username:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', info)
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if repeat_password != password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', info)
        age = request.POST.get('age')
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'registration_page.html', info)
        # print(f"Username: {username}")
        # print(f"Password: {password}")
        # print(f"Password: {repeat_password}")
        # print(f"Age: {age}")
        return HttpResponse(f"Приветствуем, {username}!")
    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    users = ['truelogin', 'Vasya', 'Peter', 'Ole']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            for user in users:
                if user == username:
                    info['error'] = 'Пользователь уже существует'
                    return render(request, 'registration_page.html', info)
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            if repeat_password != password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', info)
            age = form.cleaned_data['age']
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', info)
            return HttpResponse(f"Приветствуем, {username}!")
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})
