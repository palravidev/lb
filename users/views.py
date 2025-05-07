from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from allauth.account.forms import LoginForm, SignupForm

def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(request)
        login(request, user)
        return redirect('/')
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(
            request,
            email=form.cleaned_data['login'],
            password=form.cleaned_data['password']
        )
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')
