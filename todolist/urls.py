from django.urls import path, include
from . import views

app_name = "todolist"
urlpatterns = [
    path("", views.Intro, name="intro"),
    path("index/", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("completed/<int:todo_id>", views.completed_item, name="completed"),
    path("delete_completed/", views.deleted_completed, name="delete_completed"),
    path("delete_all", views.delete_all, name="delete_all")
]
