from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_todo/", views.add_todo, name="add_entry"),
    path("del_todo/<int:todo_id>", views.del_todo, name="del_todo")
]