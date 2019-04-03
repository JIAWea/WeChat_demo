from django.shortcuts import render
from django.shortcuts import redirect
from backend.models import *
from backend.modelForm.reportingform import ReprotingForm


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


def reporting_list(request):
    """
    报装列表信息
    :param request:
    :return:
    """
    reporting_all = Reporting.objects.all()
    return render(request,'reporting_list.html',{'reporting_all':reporting_all})

def reporting_add(request):
    """
    添加报装信息
    :param request:
    :return:
    """
    obj = ReprotingForm()           # 这里使用ModelForm进行表单验证和生成HTML
    if request.method == "POST":
        obj = ReprotingForm(data=request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('/reporting')
    return render(request,'reporting_add.html',{'obj':obj})

def reporting_edit(request,rid):
    reporting_obj = Reporting.objects.filter(id=rid).first()
    obj = ReprotingForm(instance=reporting_obj)             # instance：传入要修改数据的对象
    if request.method == "POST":
        obj = ReprotingForm(instance=reporting_obj,data=request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('/reporting')
    return render(request,'reporting_edit.html',{'obj':obj})

def reporting_delete(request,rid):
    Reporting.objects.get(id=rid).delete()
    return redirect('/reporting')
