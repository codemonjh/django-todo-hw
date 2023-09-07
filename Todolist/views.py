from .models import Todolist
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404
from .forms import TodolistForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def lists(request):
    tdlist=Todolist.objects.all()
    context={'tdlist':tdlist}
    return render(request,'Todolist/tdlists.html',context)

def detail(request,todo_id):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        to_do=Todolist.objects.get(id=todo_id)
        context={'to_do':to_do}
        return render(request,'Todolist/td_detail.html',context)

def writing(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        login_user=request.user
        if request.method=='POST':
            form=TodolistForm(request.POST)
            if form.is_valid():
                todolist = form.save(commit=False)
                todolist.author=login_user
                todolist.save()
                return redirect('Todolist:lists')
        else:

            form=TodolistForm()
        return render(request,'Todolist/writing.html',{'form': form})

def signup(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/')
    else:
        form = UserForm()
        return render(request, 'Todolist/sighup.html', {'form': form})


@login_required(login_url='Todolist:login')
def modify(request,todo_id):
    todolist = get_object_or_404(Todolist, pk=todo_id)
    if request.user != todolist.author:
        messages.error(request, '수정권한이 없다!')
        return redirect('Todolist:detail', todo_id=todolist.id)
    else:
        if request.method == "POST":
            form = TodolistForm(request.POST, instance=todolist)
            if form.is_valid():
                todolist = form.save(commit=False)
                todolist.author=request.user
                todolist.save()
                return redirect('Todolist:detail', todo_id=todolist.id)
        else:
            form = TodolistForm(instance=todolist)
            return render(request,'Todolist/writing.html',{'form':form})

def delete(request,todo_id):
    todolist=get_object_or_404(Todolist, pk=todo_id)
    todolist.delete()
    return render(request,'Todolist/deletecomplete.html')

def mytodo(request,user_id):
    user=get_object_or_404(User,id=user_id)
    userworks=Todolist.objects.filter(author=user)
    # userworks=user.todolist_set.all()
    context={'userworks':userworks}

    return render(request,'Todolist/mytodo.html',context)