from django.shortcuts import render, redirect
from .models import ToDoItem

def todo_list(request):
    todos = ToDoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        todo = ToDoItem(title=title)
        todo.save()
        return redirect('todo_list')

    return render(request, 'todo/add_todo.html')

def edit_todo(request, todo_id):
    todo = ToDoItem.objects.get(id=todo_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        todo.title = title
        todo.save()
        return redirect('todo_list')

    return render(request, 'todo/edit_todo.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = ToDoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
