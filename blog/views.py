from django.shortcuts import render

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