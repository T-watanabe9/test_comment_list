"""
URL configuration for test_comment_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app_comment_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('comment/', views.CommentView.as_view(), name='comment'),
    path('search/', views.test_search, name='search'),
    path('comment/create/', views.CreateCommentView.as_view(), name='comment_create'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
