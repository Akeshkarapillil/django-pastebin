from django.contrib.auth.decorators import login_required
from django.forms.widgets import Select
from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from user.models import Post

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def user_login(request):
    if request.method == "GET":
        # return render(request, 'login.html', {'form': AuthenticationForm()})
        return render(request, 'login.html', {'form': LoginForm()})
    
    # print(request.POST.get('username'))
    lf = LoginForm(request.POST)
    if lf.is_valid():
        username = lf.cleaned_data['username']
        password = lf.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('user_home')
        return render(request, 'login.html', {'form': lf, 'message': 'Invalid username or password'})
        
    return render(request, 'login.html', {'form': lf})

def register(request):
    if request.method == "GET":
        return render(request, 'register.html', {'form': UserCreationForm()})
    
    # If post
    ucf = UserCreationForm(request.POST)
    if ucf.is_valid():
        ucf.save()
        return redirect('login')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

def search(request):
    q = request.GET.get('s')
    if q:
        posts = Post.objects.filter(title__contains=q)
        if posts:
            pass

        res = {
            "message": f"No results found for {q}",
        }
        return render(request, 'search.html', res)
        
    return render(request, 'search.html')
