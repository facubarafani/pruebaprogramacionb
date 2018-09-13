from django.shortcuts import render, redirect
from .models import *
from .forms import ToDoForm

# Create your views here.
def home(request):
    todos = ToDo.objects.order_by('post_date')[::-1]
    todoform = ToDoForm()
    ctx = {'todos' : todos, 'todoform' : todoform}
    return render(request, 'home.html', ctx)
def submit(request):
    action_text = request.POST.get('action_text')
    task = ToDo(action_text = action_text)
    task.save()
    return redirect('home')
def delete(request,id):
    task = ToDo.objects.get(pk=id)
    task.delete()
    return redirect('home')
def archive(request,id):
    task = ToDo.objects.get(pk=id)
    task.archive = True
    task.save()
    return redirect('home')