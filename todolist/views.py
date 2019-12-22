from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import TaskList
from todolist.form import TaskForm          #for form.py
from django.contrib import messages
from django.core.paginator import Paginator

def todolist(request):
    #context = {
    #    'todolisthome_welcome_text':'Welcome to Todo list',
    #}
    #return HttpResponse("Taskpage")
    #{} is context dict passed to template

    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('New task added!'))
        return redirect('todolist')
    else: #for regular get request
        all_tasks = TaskList.objects.all()            #list of all tasks from models-db
        paginator = Paginator(all_tasks, 7)  #on which object pagination yo u want , no of recoudrds per page
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolisthome.html', {'all_tasks':all_tasks})

def contact(request):
    context = {
        'contact_welcome_text':'Welcome to contact of todo list',
    }
    return render(request, 'contact.html',context)

def about(request):
    context = {
        'about_welcome_text':'Welcome to about of todo list',
    }
    return render(request, 'about.html',context)

def deletetask(request, id):
    task = TaskList.objects.get(pk=id)
    task.delete()
    return redirect('todolist')

def edittask(request, id):
    if request.method == 'POST':
        task_obj = TaskList.objects.get(pk=id)
        form = TaskForm(request.POST or None, instance=task_obj) #not creating new instance obj, utilizing already created so instance 
        if form.is_valid:
            form.save()
        messages.success(request,('Task edited!'))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=id)
        return render(request, 'edit.html',{'task_obj':task_obj})

def completetask(request, id):
    task_obj = TaskList.objects.get(pk=id)
    task_obj.status = True
    task_obj.save()
    return redirect('todolist')

def pendingtask(request, id):
    task_obj = TaskList.objects.get(pk=id)
    task_obj.status = False
    task_obj.save()
    return redirect('todolist')

def index(request):
    return render(request, 'index.html',{})