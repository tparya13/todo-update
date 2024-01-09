from django.shortcuts import render
from .models import Task
# Create your views here.
def Home(req):
    tasks=Task.objects.all()
    if req.method=="POST":
        task=req.POST["task"]
        priority=req.POST["priority"]
        todo=Task(task=task,priority=priority)
        todo.save()
    return render(req,'index.html',{"tasks":tasks})
