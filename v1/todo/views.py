from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.utils import timezone
from django.urls import reverse

def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, "todo/index.html", {
        "todo_items":todo_items
    })

@csrf_exempt
def add_todo(request):
    data = request.POST["task_entry"]
    if data:
        entry = Todo.objects.create(added_date=timezone.now(), entry_text=data)
    # length_of_todos = Todo.objects.all().count()
    return HttpResponseRedirect(reverse("index"))

@csrf_exempt
def del_todo(request, todo_id):
    entry = Todo.objects.filter(id=todo_id)
    if entry:
        entry.delete()
    return HttpResponseRedirect(reverse("index"))
