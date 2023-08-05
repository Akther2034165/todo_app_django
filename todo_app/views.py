from django.shortcuts import render,redirect
from todo_app.forms import TodoStoreForm
from todo_app.models import TodoStoreModel
# Create your views here.

def home(request):
    if request.method == 'POST':
        todo = TodoStoreForm(request.POST)
        if todo.is_valid():
            todo.save()
            return redirect('all_todos')
    else:
        todo = TodoStoreForm()
    return render(request,'home.html',{'form': todo})

def all_todos(request):
    todo = TodoStoreModel.objects.all()
    return render(request,'all_todos.html',{'data':todo})

def edit_todos(request,id):
    todo = TodoStoreModel.objects.get(pk=id)
    form = TodoStoreForm(instance=todo)
    if request.method == 'POST':
        todo = TodoStoreForm(request.POST,instance=todo)
        if todo.is_valid():
            todo.save()
            return redirect('all_todos')
    return render(request,'home.html',{'form': form})

def delete_todos(request,id):
    todo = TodoStoreModel.objects.get(pk=id).delete()
    return redirect('all_todos')