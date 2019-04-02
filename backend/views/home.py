from django.shortcuts import render
from django.shortcuts import redirect
from backend.models import *


def index(request):
    """
    用户登录首页
    :param request:
    :return:
    """
    return render(request, 'index.html')

def articles_list(request):
    """
    文章列表，用来显示文章
    :param request:
    :return:
    """
    article_list = Article.objects.all()        # 获取所有文章
    return render(request,'articles_list.html',{'article_list':article_list})

def articles_add(request):
    """
    文章添加
    :param request:
    :return:
    """
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        user_id = request.POST.get('user_id')
        Article.objects.create(title=title,content=content,user_id=user_id)
        return redirect('/articles')

    return render(request,'articles_add.html')

def articles_edit(request,aid):
    """
    文章修改
    :param request:
    :param aid: 指定修改的文章id
    :return:
    """
    user_all = UserProfile.objects.all()
    if request.method == "GET":
        article = Article.objects.filter(id=aid).first()
        return render(request,'articles_edit.html',{'user_all':user_all,'aid':aid,'article':article})
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        user_id = request.POST.get('user_id')
        Article.objects.filter(id=aid).update(title=title, content=content, user_id=user_id)
        return redirect('/articles')

def articles_delete(request,aid):
    """
    文章删除
    :param request:
    :param aid: 指定删除的文章id
    :return:
    """
    Article.objects.filter(id=aid).delete()
    return redirect('/articles')


