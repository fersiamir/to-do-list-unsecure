import logging

from django.shortcuts import get_object_or_404, redirect, render
from django.utils.html import format_html

from .forms import TaskForm
from .models import Task

logger = logging.getLogger(__name__)


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            logger.info("Tache ajoutee (id=%s)", task.pk)
        return redirect("/")

    context = {
        "tasks": tasks,
        "form": form,
        "welcome_message": format_html("<b>{}</b>", "Bienvenue sur votre TO DO LIST !"),
    }
    return render(request, "tasks/list.html", context)


def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            logger.info("Tache modifiee (id=%s)", task.pk)
            return redirect("/")

    return render(request, "tasks/update_task.html", {"form": form})


def deleteTask(request, pk):
    item = get_object_or_404(Task, id=pk)

    if request.method == "POST":
        item.delete()
        logger.info("Tache supprimee (id=%s)", pk)
        return redirect("/")

    return render(request, "tasks/delete.html", {"item": item})
