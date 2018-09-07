from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    todos = ToDo.objects.order_by('post_date')[::-1]
    ctx = {'todos' : todos}
    return render(request, 'home.html', ctx)