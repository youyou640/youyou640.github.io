from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Article
# Create your views here.
def article_detail(request, article_id):
    #try:
        #return HttpResponse("文章id:%s" % article_id)
        #article = Article.objects.get(id=article_id)

        article = get_object_or_404(Article, pk=article_id)
        context2 = {}
        context2['article_obj'] = article
        #return HttpResponse("<h2>文章标题:%s</h2> <br> 文章内容:%s" % (article.title, article.content))
        #return render(request, "article_detail.html", context2)
        return render_to_response("article_detail.html", context2)
    #except Article.DoesNotExist:
        #raise Http404("你访问的东西不见拉")

def article_list(request):
    articles3 = Article.objects.all()
    #articles3 = Article.objects.filter(is_deleted=True)
    context3 = {}
    context3['articlesbl'] = articles3
    return render_to_response('article_list.html', context3)