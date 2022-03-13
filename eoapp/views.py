from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import TaskModel
from .forms import TaskForm

def home(request):
	if request.user.is_authenticated:
		return render(request,"home.html")
	else:
		return redirect("user_login")
	
def viewtask(request):
    user = request.user
    print(user)
    data = TaskModel.objects.filter(user=request.user)
	#task = TaskModel.objects.filter(owner=request.user)
    #data = TaskModel.objects.all()
    return render(request,'viewtask.html',{'data' : data})

#@login_required(login_url='login/')
def createtask(request):
    if request.method == 'POST':
        user = request.user
        f = TaskForm(request.POST)
        if f.is_valid():
            em = request.user.email
            print (em)

            todo = f.save(commit=False)
            todo.user = user
            todo.save()
            fm = TaskForm()
            return render(request, 'createtask.html', {'fm': fm,
                          'msg': 'Task Added'})
        else:
            return render(request, 'createtask.html', {'fm': f,
                          'msg': 'Check Errors'})
    else:
        fm = TaskForm()
        return render(request, 'createtask.html', {'fm': fm})

def delete(request,id):
    print(id)
    ds = TaskModel.objects.get(pk = id)
    ds.delete()
    return redirect('viewtask')
	
