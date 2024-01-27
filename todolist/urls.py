from django.urls import path, include
from . import views

app_name = "todolist"
urlpatterns = [
    path("", views.Intro, name="intro"),
    path("index/", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("details/<int:item_id>/", views.details, name="details"),
    path("update/<int:item_id>/", views.update, name="update"),
    path("delete/<int:item_id>/", views.delete, name="delete"),
    path("delete_all", views.delete_all, name="delete_all")
]
