from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def register(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.set_created_by(str(user.username))
            new_user.save()
            messages.success(
               request, 'congratulation {} you have registerated successfully.'.format(new_user))
            # messages.success(
            #     request, f'done {new_user} you can now login')
            return redirect('allUsers')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.htm', {
        'form': form,
    })

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            messages.warning(
                request, 'Incorrect Username or Password')
    else:
        form = LoginForm() 
    return render(request, 'login.htm', context={
        'title' : 'login',
        'form' : form,
    })

@login_required
def logout_user(request):
    logout(request)
    messages.success(
                request, 'Successfully loged out')
    return redirect('login')

@login_required
def profile(request):
    return redirect('register')

def error_404(request):
    logout(request)
    return render(request, 'error_404.htm', {
        'title' : 'error not found',
    })
@login_required
def teacher_profile(request, id):
    user = CustomUser.objects.get(pk=id)
    return render(request, 'profile.htm', {
        'user' : user,
    })

@login_required
def allUsers(request):
    all_users = CustomUser.objects.filter(created_by=request.user)
    return render(request, 'allUsers.htm', {
       'all_users' : all_users, 
    })
