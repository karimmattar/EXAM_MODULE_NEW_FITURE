from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login',),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('error_404/', views.error_404, name='error_404'),
    path('teacher_profile/<int:id>/', views.teacher_profile, name='teacher_profile'),
]
