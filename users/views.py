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
    if user.role == 'teacher':
        return redirect('teacher_profile', user.id)
    elif user.role == 'student':
        return redirect('error_404')
    elif user.role == 'parent':
        return redirect('error_404')
    elif user.role == 'headMaster':
        return redirect('error_404')
    else:
        return redirect('error_404')

def error_404(request):
    logout(request)
    return render(request, 'error_404.htm', {
        'title' : 'error not found',
    })

def teacher_profile(request, id):
    user = CustomUser.objects.get(pk=id)
    return render(request, 'profile.htm', {
        'user' : user,
    })
