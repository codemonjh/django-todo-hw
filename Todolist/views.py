from .models import Todolist
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# Create your views here.

def lists(request):
    tdlist=Todolist.objects.all
    context={'tdlist':tdlist}
    return render(request,'Todolist/tdlists.html',context)

def detail(request,todo_id):
    to_do=Todolist.objects.get(id=todo_id)
    context={'to_do':to_do}
    return  render(request,'Todolist/td_detail.html',context)

def writing(request):
    return render(request,'Todolist/writing.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('lists')
    else:
        form = UserForm()
    return render(request, 'Todolist/sighup.html', {'form': form})
