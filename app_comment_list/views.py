import json
from typing                     import Any
from django.db.models.query     import QuerySet
from django.forms import BaseModelForm
from django.http                import HttpRequest
from django.http.response       import HttpResponse , JsonResponse
from django.shortcuts           import render , redirect
from django.views.generic       import ListView
from django.views.generic.edit  import CreateView
from django.contrib.auth.views  import LoginView , LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models                    import Comment
from django.views.decorators.csrf import csrf_protect















 
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

     # ビュー呼び出し時、クエリセットをログイン済ユーザーに絞って返す。
     def get_queryset(self):
           user = self.request.user
           return Comment.objects.filter(user= user) 
     
     # ビュー呼び出し時に呼び出し。
     def get(self, request, *args, **kwargs):
          return super().get(self, request, *args, **kwargs)
     
     def post(self, request, *args, **kwargs):
          # return super().post(self, request, *args, **kwargs)
          print("コメントビュー!post関数!")
          return JsonResponse({'message': 'データが正常に保存されました。'})
     





























# コメント新規作成ビュー。
class CreateCommentView(LoginRequiredMixin , CreateView):
     template_name = "comment_create.html"
     model = Comment
     fields = ['category' , 'content']
     
     # フォーム入力時に呼び出し。
     def form_valid(self, form: BaseModelForm) :
          # 新規作成フォームにて、userフィールドは必ずログインユーザーとする。
          form.instance.user = self.request.user
          return super().form_valid(form)



# ログアウトビュー。
class LogoutView(LogoutView):
     template_name = 'top.html'


# サーチ関数。
def test_search(request):
     print('サーチ関数だよ！！!')
     print(request)
     # リクエストのbodyを辞書型に変換
     dic = json.loads(request.body)
     print(dic)
     print(dic.get('model'))
     data = {'data' : 'あああ'}
     return JsonResponse(data)





