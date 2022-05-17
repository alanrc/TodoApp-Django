from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def index(request):
    num_task =Task.objects.count()
    tasks = Task.objects.all()
    # tasks = Task.objects.order_by('created')
    
    if request.method == 'POST':
        formTask = TaskForm(request.POST)
        if formTask.is_valid():
            formTask.save()
            return redirect('index')
    else:
        formTask = TaskForm()
    
        context = {'num_task':num_task,'tasks':tasks, 'formTask': formTask}
    
        return render(request,'index.html', context)

def editTask(request, id):
    task = get_object_or_404(Task,pk=id)
    if request.method == 'POST':
        formTask = TaskForm(request.POST, instance=task)
        if formTask.is_valid():
            formTask.save()
            return redirect('index')
    else:
        formTask = TaskForm(instance=task)
        return render(request,'edit.html', {'formTask': formTask})
    

def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    if task:
        task.delete()
    return redirect('index')

