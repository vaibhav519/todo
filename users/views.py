from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
            messages.success(
                request, f'Your account has been created ! You are now able to login ')
            return redirect('todo-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo-home')
        else:
            messages.info(request, "Username or password is incorrect",
                          extra_tags="incorrect_details")

    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)
