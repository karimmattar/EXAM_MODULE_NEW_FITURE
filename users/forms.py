from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, ROLES

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=30,
                               help_text='not include spaces')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput(), min_length=8)
        
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2', 'avatar', 'phone_number', 'role',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('password not valid')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if CustomUser.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('user name is exist')
        return cd['username']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name',
                  'last_name', 'avatar', 'phone_number', 'role',)

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Usename or Email')
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('username', 'password',)