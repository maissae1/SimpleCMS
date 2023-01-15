from django.shortcuts import render
from posts.forms import LoginForm


def index(request):
    return render(request, 'base.html')

def login_view(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)

    else:
        loginForm = LoginForm()

    return render(request, 'login.html', {'form': loginForm})
