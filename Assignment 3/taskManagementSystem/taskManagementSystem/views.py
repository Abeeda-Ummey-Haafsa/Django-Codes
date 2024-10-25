from django.shortcuts import render
from task.models import Task
from category.models import Category

def show_task(request):
    # return HttpResponse("This is the task list page")
    data = Task.objects.all()
    return render(request, 'show_task.html', {'data': data})