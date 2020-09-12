from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model): #创建一个类,引用model
	title = models.CharField(max_length=31) #这个表有2个字段，title和content，字段类型是字符和文本
	content = models.TextField()
	created_time = models.DateTimeField(auto_now_add=True)
	last_updated_time = models.DateTimeField(auto_now=True)
	auther = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
	is_deleted = models.BooleanField(default=False)
	readed_num = models.IntegerField(default=0)

def __str__(self):  # 为Article类添加的一个方法,这个方法的内容就是return一个东西
		return "<Article: %s>" % self.title

	#created_time = models.DateTimeField(default=timezone.now)