from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('groups/', views.groups_view, name='groups'),
    path('account/', views.account_view, name='account'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]


def home(request):
    return render(request, 'blog/home.html')

def login_view(request):
    return render(request, 'blog/login.html')

def register_view(request):
    return render(request, 'blog/register.html')

def groups_view(request):
    return render(request, 'blog/groups.html')

def account_view(request):
    return render(request, 'blog/account.html')