from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from backend.models import *
from backend.modelForm.reportingform import ReprotingForm
from backend.modelForm.repairform import RepairForm
from django.contrib.auth.decorators import login_required
import json,os
from django.views.decorators.csrf import csrf_exempt    # 局部屏蔽csrf
from WeChatPM.settings import MEDIA_UPLOAD_IMGS

# 后台首页
@login_required
def index(request):
    no_done_num = Reporting.objects.filter(status=0).count()  # 未处理
    repair_no_done_num = TroubleShoot.objects.filter(status=0).count()  # 未处理
    return render(request, 'index.html',
                  {'no_done_num':no_done_num,
                   'repair_no_done_num':repair_no_done_num}
                  )

# 文章列表
@login_required
def articles_list(request):
    article_list = Article.objects.all()        # 获取所有文章

    return render(request,'articles_list.html',{'article_list':article_list})

# 文章添加
@login_required
def articles_add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        user_id = request.POST.get('user_id')
        if title and content and user_id:
            Article.objects.create(title=title,content=content,user_id=user_id)
            return redirect('/articles')
        else:
            return HttpResponse(json.dumps({'status':404,'error_msg':'不能为空'}))
    return render(request,'articles_add.html')

# 文章修改
@login_required
def articles_edit(request,aid):
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

# 文章删除
@login_required
def articles_delete(request,aid):
    Article.objects.filter(id=aid).delete()
    return redirect('/articles')

# 报装信息列表
@login_required
def reporting_list(request):
    reporting_all = Reporting.objects.all()
    return render(request,'reporting_list.html',{'reporting_all':reporting_all})

# 报装信息添加
@login_required
def reporting_add(request):
    obj = ReprotingForm()           # 这里使用ModelForm进行表单验证和生成HTML
    if request.method == "POST":
        obj = ReprotingForm(data=request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('/reporting')
    return render(request,'reporting_add.html',{'obj':obj})

# 报装信息修改
@login_required
def reporting_edit(request,rid):
    reporting_obj = Reporting.objects.filter(id=rid).first()
    obj = ReprotingForm(instance=reporting_obj)             # instance：传入要修改数据的对象
    if request.method == "POST":
        obj = ReprotingForm(instance=reporting_obj,data=request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('/reporting')
    return render(request,'reporting_edit.html',{'obj':obj})

# 报装信息删除
@login_required
def reporting_delete(request,rid):
    Reporting.objects.get(id=rid).delete()
    return redirect('/reporting')


# 报修列表
def repair_list(request):
    repair_all = TroubleShoot.objects.all()
    return render(request,'repair_list.html',{'repair_all':repair_all})

# 报修添加
def repair_add(request):
    obj = RepairForm()  # 这里使用ModelForm进行表单验证和生成HTML
    if request.method == "POST":
        obj = RepairForm(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            return redirect('/repair')
    return render(request, 'repair_add.html', {'obj': obj})


# 文章图片
@csrf_exempt
def img_upload(request):
    ret = {'error':0,'url':''}
    upload_img = request.FILES.get('imgFile')
    name = upload_img.name
    # with open(os.path.join(MEDIA_UPLOAD_IMGS,name),'w') as f:
        # for line in upload_img.chunk():
        #     f.write(line)
    return HttpResponse(json.dumps(ret))
