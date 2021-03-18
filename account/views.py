from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


def register(request):
    if request.user.is_anonymous:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'{username} registered successfully!')
                return redirect('/login')
        context = {'form': form}
        return render(request, 'pages/register.html', context=context)
    else:
        return redirect('/')


def login_page(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'username or password is incorrect')
        return render(request, 'pages/login.html', context={})
    else:
        return redirect('/')


def logout_page(request):
    logout(request)
    return redirect('/login')