from django.shortcuts import render, redirect
from datetime import datetime
from blog.wallet import wallet
# from .db import mydb
from .models import Todo, Country


# Create your views here.
def home(request):
    title = 'Главная страница'
    return render(request, 'home.html', {
        'title': title
    })


def about(request):
    title = 'Страница О нас'
    return render(request, 'about.html', {
        'title': title
    })


def time(request):
    title = 'Страница показа времени'
    time_now = datetime.now()
    return render(request, 'time.html', {
        'time_now': time_now,
        'title': title
    })


def mywallet(request):
    return render(request, 'mywallet.html', {
        'wallet': wallet
    })


def todo(request):
    todos_list = Todo.objects.all()

    return render(request, 'todo.html', {
        'todos': todos_list
    })


def todo_add(request):
    todo_form_name = request.GET.get('todo_name')
    new_todo = Todo(todo_name = todo_form_name)
    new_todo.save()

    return redirect('/todo')


def todo_delete(request):
    todo_id = request.GET.get('todo_id')
    todo = Todo.objects.get(id = todo_id)

    print('Мага TODo ID келди: ', todo_id)
    print('Базадан таптым: ', todo.todo_name)

    if int(todo_id) > 1:
        deleted = todo.delete()

    print('Базадан очурдум: ')
    return redirect('/todo')





def countries(request):
    country_list = Country.objects.all()
    return render(request, 'country_list.html', {'countries': country_list})

def countries_add(request):
    new_country_name = request.GET.get('country_name')
    new_country = Country(country_name = new_country_name)
    new_country.save()
    return redirect('/countries')

def country_delete(request):
    country_id = request.GET.get('country_id')
    country = Country.objects.get(id = country_id)

    if int(country_id) > 1:
        deleted = country.delete()

    return redirect('/countries')