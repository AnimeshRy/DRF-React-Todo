from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls.base import reverse
from .models import *
from .forms import TaskForm

def index(request):
    alltasks = Task.objects.all().order_by('-time_added')

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'alltasks': alltasks, "form":form}
    return render(request, "todo/index.html", context)

def update(request, id):
    currTask = Task.objects.get(id=id)

    form = TaskForm(instance=currTask)
    if request.method=='POST':
        form = TaskForm(request.POST, instance=currTask)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("todos:index"))

    context = {'form': form, 'currTask': currTask}
    return render(request, 'todo/update.html', context)

def delete(request, id):
    task = Task.objects.filter(id=id)
    if task:
        task.delete()
    return HttpResponseRedirect(reverse("todos:index"))
