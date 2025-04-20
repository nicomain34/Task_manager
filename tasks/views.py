from django.shortcuts import render, redirect
from .models import Task
from django.shortcuts import get_object_or_404, redirect
from .forms import TaskForm

def task_list(request):
    sort = request.GET.get('sort', 'created')

    if sort == 'deadline':
        tasks = Task.objects.order_by('deadline')  # дедлайн ближчий — вище
    elif sort == 'created':
        tasks = Task.objects.order_by('-created_at')  # нові задачі — зверху
    else:
        tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'form': form
    })

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

