from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import TaskToComplete
from .form import TaskToCompleteForm


# Create your views here.

def Intro(request):
    return HttpResponse("Hello World!")


def index(request):
    todo_items = TaskToComplete.objects.all()
    form = TaskToCompleteForm()
    return render(request, "todolist/index.html", {"todo_items": todo_items, "form": form})


def add(request):
    form = TaskToCompleteForm(request.POST or None)
    if form.is_valid():
        new_todo = TaskToComplete(task=request.POST['task'])
        new_todo.save()
    return redirect("todolist:index")


def completed_item(request, todo_id):
    todo = TaskToComplete.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect("todolist:index")


def deleted_completed(request):
    completed_todo = TaskToComplete.objects.filter(completed__exact=True)
    completed_todo.delete()
    return redirect("todolist:index")


def delete_all(request):
    tasks = TaskToComplete.objects.all()
    tasks.delete()
    return redirect("todolist:index")
