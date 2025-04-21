from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    # Фільтрація
    filter_option = request.GET.get('filter', 'all')
    
    if filter_option == 'completed':
        tasks = Task.objects.filter(completed=True)
    elif filter_option == 'incomplete':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()

    # Сортування
    sort_option = request.GET.get('sort', 'created')
    if sort_option == 'deadline':
        tasks = tasks.order_by('deadline')
    elif sort_option == 'completed':
        tasks = tasks.order_by('completed')  # невиконані будуть вгорі
    else:
        tasks = tasks.order_by('-created_at')

    # Обробка форми
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form,
        'filter_option': filter_option
    }
    return render(request, 'tasks/task_list.html', context)


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
