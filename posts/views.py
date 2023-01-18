from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from posts.forms import LoginForm

@login_required
def index(request):
    return render(request, 'base.html')

def login_view(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is None:
                # TODO: flash error message
                pass
            else:
                login(request, user)
                return redirect('home')

    else:
        loginForm = LoginForm()

    return render(request, 'login.html', {'form': loginForm})
