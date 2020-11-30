from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
from .models import * 
from .forms import *


def index(request):
    tasks = Task.objects.all()
    form  = TaskForm()
    context = {'tasks' : tasks , 'form' : form}
    
    if request.method == "POST":
        form  = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    

    return render(request,'tasks/list.html',context)

def update_task(request , prk):
    task = Task.objects.get(id = prk)
    form = TaskForm(instance=task)
    
    context = {'form': form }
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.update = True
            form.save()
            return redirect("/")
    
    return render(request, "tasks/update_task.html", context)


def delete_task(request, prk):
    item = Task.objects.get(id = prk)
    context = {'item':item}
    
    if request.method == 'POST':
        item.delete()
        return redirect("/")

    return render(request,"tasks/delete.html" , context)

