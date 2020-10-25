from django.http import HttpResponse,Http404,HttpResponseRedirect

from django.shortcuts import render

from .models import Article

def index(request):
    latest_article_list = Article.objects.order_by('-article_pubdate')[:3]
    return  render(request, 'articles/list.html', {'latest_article_list': latest_article_list})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('NO')
    return render(request,'articles/detail.html',{'article':a})

def test(request):
    return HttpResponse('hi')