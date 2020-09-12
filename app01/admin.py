from django.contrib import admin
from .models import Article
@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin): #为Article定义一个管理类
    list_display = ("id","title", "content","created_time","last_updated_time","auther","is_deleted","readed_num")
    ordering = ("-id",)


# Register your models here.
#admin.site.register(Article,ArticleAdmin)
