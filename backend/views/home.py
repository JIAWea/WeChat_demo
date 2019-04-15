from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from backend.models import *
import json,os
from django.views.decorators.csrf import csrf_exempt    # 局部屏蔽csrf
from WeChatPM.settings import MEDIA_UPLOAD_IMGS
from django.contrib.auth.decorators import login_required
from backend.permissions.check_permission import check_permission
from backend.modelForm.articleForm import articleForm
from backend.modelForm.infomationForm import infomationForm


# 后台首页
@login_required
def index(request):
    return render(request, 'index.html',)

# 文章列表
@check_permission('backend.article_manager')
@login_required
def articles_list(request):
    article_list = Article.objects.all().order_by('-id')       # 获取所有文章
    return render(request,'articles_list.html',{'article_list':article_list})

# 文章添加
def articles_add(request):
    obj = articleForm()
    if request.method == "POST":
        obj = articleForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('/backend/articles/')
    return render(request, 'article_add.html',{'obj':obj})

# 文章编辑
@check_permission('backend.article_manager')
@login_required
def article_edit(request,aid):
    article_obj = Article.objects.filter(id=aid).first()
    obj = articleForm(instance=article_obj)
    if request.method == "POST":
        obj = articleForm(instance=article_obj,data=request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('/backend/articles/')
    return render(request, 'article_edit.html', {'obj': obj,'aid':aid})
    # if request.method == "GET":
    #     article = Article.objects.filter(id=aid).first()
    #     return render(request, 'article_edit.html', {'aid':aid, 'article':article})
    # else:
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     if not title:
    #         return render(request,'article_edit.html',{'err_msg':'标题不能为空'})
    #     if not content:
    #         return render(request, 'article_edit.html', {'err_msg': '内容不能为空'})
    #     Article.objects.filter(id=aid).update(title=title, content=content)
    #     return redirect('/backend/articles/')

# 文章删除
@check_permission('backend.article_manager')
@login_required
def article_delete(request,aid):
    if aid:
        Article.objects.filter(id=aid).delete()
    return redirect('/backend/articles/')


# 公告列表
@check_permission('backend.info_manager')
@login_required
def infomation_list(request):
    infomation = Info.objects.all().order_by('-id')
    return render(request, 'infomation_list.html', {'infomation':infomation})

# 公告添加
@check_permission('backend.info_manager')
@login_required
def infomation_add(request):
    obj = infomationForm()
    if request.method == "POST":
        obj = infomationForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('/backend/infomation/')
    return render(request, 'infomation_add.html', {'obj': obj})

# 公告删除
@check_permission('backend.info_manager')
@login_required
def infomation_delete(request,iid):
    if iid:
        Info.objects.filter(id=iid).delete()
    return redirect('/backend/infomation/')

# 公告编辑
@check_permission('backend.info_manager')
@login_required
def infomation_edit(request,iid):
    info_obj = Info.objects.filter(id=iid).first()
    obj = infomationForm(instance=info_obj)
    if request.method == "POST":
        obj = infomationForm(instance=info_obj, data=request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('/backend/infomation/')
    return render(request, 'infomation_edit.html', {'obj': obj, 'iid': iid})


# ########################################## 报装相关 ########################################


# 报装信息列表
@check_permission('backend.reporting_manager')
@login_required
def reporting_list(request):
    reporting_all = Reporting.objects.all().order_by('-id')
    if request.method == "POST":
        content = request.body  # 字节
        content = str(content, encoding='utf-8')  # 字符串
        result = json.loads(content)
        # print('结果', type(result))               # [1,2,3]
        response = {'status': False, 'msg': None}
        for id in result:
            if id:
                obj = Reporting.objects.filter(id=id).first()
                if obj.status == 1:
                    response['msg'] = '已经处理过了'
                else:
                    Reporting.objects.filter(id=id).update(status=1)
                    response['status'] = True
                    response['msg'] = '设置成功'
            else:
                response['msg'] = '设置失败'
        return JsonResponse(response)
    return render(request,'reporting_list.html',{'reporting_all':reporting_all})

# 报装信息删除
@check_permission('backend.reporting_manager')
@login_required
def reporting_delete(request):
    if request.method == "POST":
        content = request.body  # 字节
        content = str(content, encoding='utf-8')  # 字符串
        result = json.loads(content)
        # print('结果', type(result))               # [1,2,3]
        response = {'status': False, 'msg': None}
        for id in result:
            if id:
                obj = Reporting.objects.filter(id=id).first()
                if not obj:
                    response['msg'] = '该信息已经被删除过了'
                else:
                    Reporting.objects.filter(id=id).delete()
                    response['status'] = True
                    response['msg'] = '删除成功'
            else:
                response['msg'] = '删除失败'
        return JsonResponse(response)


# ########################################## 报修相关 ########################################

# 报修列表
@login_required
@check_permission('backend.repair_manager')
def repair_list(request):
    repair_all = TroubleShoot.objects.all().order_by('-id')
    if request.method == "POST":
        content = request.body  # 字节
        content = str(content, encoding='utf-8')  # 字符串
        result = json.loads(content)
        # print('结果', type(result))               # [1,2,3]
        response = {'status': False, 'msg': None}
        for id in result:
            if id:
                obj = TroubleShoot.objects.filter(id=id).first()
                if obj.status == 1:
                    response['msg'] = '已经处理过了'
                else:
                    TroubleShoot.objects.filter(id=id).update(status=1)
                    response['status'] = True
                    response['msg'] = '设置成功'
            else:
                response['msg'] = '设置失败'
        return JsonResponse(response)
    return render(request,'repair_list.html',{'repair_all':repair_all})

# 报修删除
@check_permission('backend.repair_manager')
@login_required
def repair_delete(request):
    if request.method == "POST":
        content = request.body  # 字节
        content = str(content, encoding='utf-8')  # 字符串
        result = json.loads(content)
        # print('结果', type(result))               # [1,2,3]
        response = {'status': False, 'msg': None}
        for id in result:
            if id:
                obj = TroubleShoot.objects.filter(id=id).first()
                if not obj:
                    response['msg'] = '该信息已经被删除过了'
                else:
                    TroubleShoot.objects.filter(id=id).delete()
                    response['status'] = True
                    response['msg'] = '删除成功'
            else:
                response['msg'] = '删除失败'
        return JsonResponse(response)


# ########################################## 文章图片 ########################################

# 文章图片
@csrf_exempt
def img_upload(request):
    response = {'error':0,'url':None,'message':None}
    if request.method == "POST":
        upload_img = request.FILES.get('uploadImg')
        if upload_img:
            with open(os.path.join(MEDIA_UPLOAD_IMGS,upload_img.name),'wb') as f:
                for line in upload_img.chunks():
                    f.write(line)
            # path = os.path.join(MEDIA_UPLOAD_IMGS,upload_img.name)
            # response['url'] = 'http:127.0.0.1:8000/%s' % str(path)      # 返回url路径
            print('--------------------',upload_img.name)
            response['url'] = str(upload_img.name)                      # 返回url路径
        else:
            response['error'] = 1
            response['message'] = '上传失败'
    # print('返回信息',response)
    return JsonResponse(response)

# 图片显示
def img_show(request,name):
    with open(os.path.join(MEDIA_UPLOAD_IMGS,name), 'rb') as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type="image/png")
# 图片显示
def img_edit_show(request,aid,name):
    with open(os.path.join(MEDIA_UPLOAD_IMGS,name), 'rb') as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type="image/png")


# 无权限
def permission_denied(request):
    return render(request,'403.html')