from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render , redirect
from django.views.generic import TemplateView , ListView
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment

 # Create your views here.

 
# 未ログインユーザーがURLにアクセスしたときのリダイレクト先
# 新規登録ボタン
# ログインフォーム
# ログアウト時のリダイレクト先
class LoginView(LoginView):
     template_name = 'login.html'
     
     # もしユーザーがログイン済みだったらhome.htmlにリダイレクト。
     def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
          if request.user.is_authenticated:
               return redirect("home")
          return super().dispatch(request, *args, **kwargs)

# ボツ。
'''
class TopView(LoginView):
     template_name = 'top.html'
'''

class HomeView(LoginRequiredMixin , TemplateView):
     template_name = "home.html"
     def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
          if request.user.is_authenticated:
               print('ホームビュー！')
          return super().dispatch(request, *args, **kwargs)

class CommentListView(ListView):
     template_name = "comment_list.html"
     model = Comment
     def get_queryset(self):
           user = self.request.user
           print(user)
           return Comment.objects.filter(user = user) # ログインせずに呼び出すとエラー。エラーの理由はしらね。
     # 今ログインしているユーザー
     # def get_queryset(self) -> QuerySet[Any]:
     #      return super().get_queryset()



class LogoutView(LogoutView):
     template_name = 'top.html'
     def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
          print('ログアウトしました！:' + request.user.username)
          return super().dispatch(request, *args, **kwargs)
