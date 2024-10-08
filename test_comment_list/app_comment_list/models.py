from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# コメントモデル。
class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)   # コメントID。主キー。
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE) # 外部キー。デフォルトユーザーモデル。
    category = models.CharField(max_length=255) # コメントカテゴリ。
    content = models.TextField(null=True , blank=True) # コメント内容。
    datetime = models.DateTimeField(default=timezone.now) # 投稿した時刻。