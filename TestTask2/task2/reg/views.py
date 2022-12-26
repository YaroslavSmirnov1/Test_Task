from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, NumberForm
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required                                                       #здесь мы ставим обязательную авторизацию на страницы профиля и Марко Поло
def profile(request):
    return render(request, 'profile.html')


@login_required
def markopolo(request):
    if request.method == 'POST':

        form = NumberForm(request.POST)
        if form.is_valid():

            int_start = form.cleaned_data['interval_start_field']      #здесь мы получаем списки из данных, введённых в формы
            int_finish = form.cleaned_data['interval_finish_field']
            list_data = form.cleaned_data['list_field'].split()
            if list_data is None:                                      #проверка на случай, если поле не заполнено. Тогда вместо None мы создаём пустой список
                list_data = []
            numbers = []                                                #numbers - это список цифровых символов, введённых в форму
            text_list = []
            for element in list_data:                                   #перебираем массив из поля со списком, переводим символы в тип integer и добавляем в массив numbers
                if element.isdigit():
                    numbers.append(int(element))
            if int_start and int_finish is not None:                                    #проверка на то, что поля ввода промежутка не пустые. В этом случае мы составляем список значений и пополняем им список из первого поля
                numbers = numbers + list(range(int_start, int_finish + 1))
            for number in numbers:
                if number % 3 == 0 and number % 5 == 0 and number != 0:                 #здесь проверки на возможность деления чисел без остатка на заданные числа, а также последующее добавление соответствующих слов в список text_list
                    text_list.append('МаркоПоло' + '\n')
                elif number % 3 == 0 and number != 0:
                    text_list.append('Марко' + '\n')
                elif number % 5 == 0 and number != 0:
                    text_list.append('Поло' + '\n')
                else:
                    text_list.append('Число не соответствует условиям' + '\n')
            return HttpResponse(text_list)
        else:
            return render(
                request,
                'markopolo.html',
                context={'form': form},
            )
    else:
        form = NumberForm()                                                             #отрисовка формы, если form.is_valid не выполняется
        return render(
            request,
            'markopolo.html',
            context={'form': form},
        )
