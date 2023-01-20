from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from posts.forms import LoginForm, AccountForm

@login_required
def index(request):
    return render(request, 'home.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def accounts(request):
    User = get_user_model()
    accounts = User.objects.all()

    return render(request, 'accounts.html', {'accounts': accounts})

@login_required
def create_account(request):
    if request.method == 'POST':
        accountForm = AccountForm(request.POST)

        if accountForm.is_valid():
            username = accountForm.cleaned_data['username']
            email = accountForm.cleaned_data['email']
            password = accountForm.cleaned_data['password']
            confirm_password = accountForm.cleaned_data['confirm_password']
            role = accountForm.cleaned_data['role']

            if role == 'admin':
                is_superuser = True
                is_staff = True

            elif role == 'editor':
                is_superuser = False
                is_staff = True
            
            else:
                is_superuser = False
                is_staff = False

            User = get_user_model()
            user = User.objects.create_user(
                username = username,
                email = email,
                password = password,
                is_superuser = is_superuser,
                is_staff = is_staff
            )

            user.save()

            return redirect('accounts')
    
    else:
            accountForm = AccountForm()

    return render(request, 'create_account.html', {'form': accountForm})

@login_required
def update_account(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)

    if request.method == 'POST':
        accountForm = AccountForm(request.POST, initial={
            'username': user.username,
            'email': user.email,
            'role': 'admin' if user.is_superuser else 'editor' if user.is_staff else 'author'
        })

        if accountForm.is_valid():
            username = accountForm.cleaned_data['username']
            email = accountForm.cleaned_data['email']
            password = accountForm.cleaned_data['password']
            role = accountForm.cleaned_data['role']

            if role == 'admin':
                is_superuser = True
                is_staff = True

            elif role == 'editor':
                is_superuser = False
                is_staff = True

            else:
                is_superuser = False
                is_staff = False

            user.username = username
            user.email = email

            if password:
                user.set_password(password)

            user.is_superuser = is_superuser
            user.is_staff = is_staff
            user.save()

            return redirect('accounts')
    else:
        accountForm = AccountForm(initial={
            'username': user.username,
            'email': user.email,
            'role': 'admin' if user.is_superuser else 'editor' if user.is_staff else 'author'
        })

    return render(request, 'update_account.html', {'form': accountForm})

@login_required
def delete_account(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)
    user.delete()

    return redirect('accounts')


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
