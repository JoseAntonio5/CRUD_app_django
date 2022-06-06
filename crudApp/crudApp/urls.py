"""crudApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('user/<id>/', views.userPage, name='userPage'),
    path('posts/', views.index, name='posts'),
    path('posts/new/', views.createPost, name='new'),
    path('posts/<id>/', views.viewPostDetails, name='details'),
    path('posts/<id>/update/', views.updatePost, name='update'),
    path('posts/<id>/delete/', views.deletePost, name='delete'),
    path('error/', views.errorPage, name='error'),
    path('logout/', views.logoutUser, name='logout'),
]
