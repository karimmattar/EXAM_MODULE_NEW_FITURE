from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            messages.success(
               request, 'congratulation {} you have registerated successfully.'.format(new_user))
            # messages.success(
            #     request, f'done {new_user} you can now login')
            return redirect('login')
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
            return redirect('profile')
        else:
            messages.warning(
                request, 'Incorrect Username or Password')
    else:
        form = LoginForm() 
    return render(request, 'login.htm', context={
        'title' : 'login',
        'form' : form,
    })

def logout_user(request):
    logout(request)
    messages.success(
                request, 'Successfully loged out')
    return redirect('login')

def profile(request):
    user = request.user
    return render(request, 'profile.htm', {
        'user' : user,
    })
