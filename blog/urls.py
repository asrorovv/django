from django.urls import path
from views import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('groups/', views.groups_view, name='groups'),
    path('account/', views.account_view, name='account'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

