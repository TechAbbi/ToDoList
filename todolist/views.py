from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import TaskToComplete
from .form import TaskToCompleteForm


# Create your views here.

def Intro(request):
    return HttpResponse("Hello World!")


def index(request):
    todo_items = TaskToComplete.objects.all()
    return render(request, "todolist/index.html", {"todo_items": todo_items})


def add(request):
    form = TaskToCompleteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("todolist:index")
    else:
        form = TaskToCompleteForm()
    return render(request, "todolist/add.html", {"form": form})


def details(request, item_id):
    item = TaskToComplete.objects.get(pk=item_id)
    return render(request, "todolist/details.html", {"item": item})


def update(request, item_id):
    item = TaskToComplete.objects.get(pk=item_id)
    form = TaskToCompleteForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("todolist:index")
    return render(request, "todolist/add.html", {"form": form, "item": item})


def delete(request, item_id):
    item = TaskToComplete.objects.get(pk=item_id)
    if request.method == "POST":
        item.delete()
        return redirect("todolist:index")
    return render(request, "todolist/delete.html", {"item": item})

def delete_all(request):
    tasks = TaskToComplete.objects.all()
    if request.method == "POST":
        tasks.delete()
        return redirect("todolist:index")
    return render(request, "todolist/delete_all.html", {"tasks": tasks})
