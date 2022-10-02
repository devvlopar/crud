from django.shortcuts import render
from django.http import JsonResponse
from crud_app.models import Task, User

# Create your views here.
def index(request):
    all_users = User.objects.all()
    return render(request, 'index.html', {'all_users':all_users})

def create_task(request):
    all_users = User.objects.all()
    if request.method == 'POST':

        Task.objects.create(

            user = User.objects.get( id = int(request.POST['user']) ),
            name = request.POST['task'],
            description = request.POST['description'],
            category = request.POST['category'],

        )

        return render(request, 'index.html', {'msg': 'Task Created Successfully!!', 'all_users':all_users})
    else:
        return render(request, 'index.html', {'all_users':all_users})

def show_tasks(request):
    all_tasks = Task.objects.all()
    return render(request, 'show_tasks.html', {'all_tasks':all_tasks})


def delete_task(request, pk):
    id = pk
    d_task = Task.objects.get(id = id)
    d_task.delete()

    all_tasks = Task.objects.all()
    return render(request, 'show_tasks.html', {'all_tasks':all_tasks}) 

def complete_task(request, pk):
    id = pk
    c_task = Task.objects.get(id = id)
    c_task.status = True 
    c_task.save()
    all_tasks = Task.objects.all()
    return render(request, 'show_tasks.html', {'all_tasks':all_tasks}) 