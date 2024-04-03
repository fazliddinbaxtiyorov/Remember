from django.shortcuts import render, redirect, get_object_or_404
from .models import Remember
from .forms import RememberForm


# Create your views here.
def home(request):
    remember = Remember.objects.all()
    return render(request, 'index.html', {'remember': remember})


def adding(request):
    if request.method == 'POST':
        form = RememberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RememberForm()
    return render(request, 'add.html', {'form': form})


def update(request, task_id):
    task = get_object_or_404(Remember, id=task_id)
    if request.method == 'POST':
        form = RememberForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('/')
    else:
        form = RememberForm(instance=task)
    return render(request, 'update.html', {'form': form, 'task': task})


def delete(request, task_id):
    task = get_object_or_404(Remember, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task': task})

