from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма невірна'

    form = TodoForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
