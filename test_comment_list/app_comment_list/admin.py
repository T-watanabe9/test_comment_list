from django.contrib import admin
from .models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
     list_display = ('__str__' , 'user', 'category', 'datetime')
     search_fields = ('name',)
admin.site.register(Comment , CommentAdmin)

