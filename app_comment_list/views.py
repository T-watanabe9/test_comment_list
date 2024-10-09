from typing                     import Any
from django.db.models.query     import QuerySet
from django.http                import HttpRequest
from django.http.response       import HttpResponse
from django.shortcuts           import render , redirect
from django.views.generic       import ListView
from django.views.generic.edit  import CreateView
from django.contrib.auth.views  import LoginView , LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models                    import Comment

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



# ホーム画面
class HomeView(LoginRequiredMixin , ListView):
     template_name = "home.html"
     model = Comment
     
     # クラスベースビューの呼び出し時、クエリセットをログインユーザーのもののみに絞って返す。
     def get_queryset(self):
           current_user = self.request.user
           return Comment.objects.filter(user= current_user) 
     

# コメント画面。
class CommentView(LoginRequiredMixin , ListView):
     template_name = "comment.html"
     model = Comment
     def get_queryset(self):
           user = self.request.user
           return Comment.objects.filter(user= user) 
     


# コメント新規作成ビュー。
class CreateCommentView(LoginRequiredMixin , CreateView):
     template_name = "comment_create.html"
     model = Comment
     fields = '__all__'
     # def dispatch(self, request, *args, **kwargs):
     #      return super().dispatch(request, *args, **kwargs)



# ログアウトビュー。
class LogoutView(LogoutView):
     template_name = 'top.html'
