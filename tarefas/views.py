from django.shortcuts import get_object_or_404, redirect, render

from tarefas.forms import TaskForm
from .models import Task

def home(request):
    tasks = Task.objects.all()
    total_tasks = tasks.count()
    completed_tasks = 0
    remaining_tasks = total_tasks - completed_tasks
    pct = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

    for task in tasks:
        if task.done == True:
            completed_tasks += 1

    return render(
        request,
        'tarefas/home.html',
        {
            'tasks': tasks,
            'total': total_tasks,
            'completed':completed_tasks,
            'remaining': remaining_tasks,
            'pct': pct
        }
        )

def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('home')

def toggle(request, id):
    task = get_object_or_404(Task, id=id)
    task.done = not task.done
    task.save()
    return redirect('home')

def delete(request, id):

    task = get_object_or_404(Task, id=id)
    task.delete()

    return redirect("home")
