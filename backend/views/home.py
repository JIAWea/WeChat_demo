from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from backend.models import *
from backend.modelForm.reportingform import ReprotingForm
from backend.modelForm.repairform import RepairForm
from django.contrib.auth.decorators import login_required
import json,os
from django.views.decorators.csrf import csrf_exempt    # 局部屏蔽csrf
from WeChatPM.settings import MEDIA_UPLOAD_IMGS
from django.views import View

# 后台首页
@login_required
def index(request):
    # no_done_num = Reporting.objects.filter(status=0).count()  # 未处理
    # repair_no_done_num = TroubleShoot.objects.filter(status=0).count()  # 未处理
    return render(request, 'index.html',
                  # {'no_done_num':no_done_num,
                  #  'repair_no_done_num':repair_no_done_num}
                  )

# 文章列表
@login_required
def articles_list(request):
    article_list = Article.objects.all()        # 获取所有文章
    # data = []
    # for article in article_list:
    #     data_dict = {}
    #     data_dict["title"] = article.title
    #     data_dict["content"] = article.content
    #
    #     data.append(data_dict)
    # # print('文章列表',data)        [{'title': '关于公司', 'content': '<strong>哈哈哈</strong>'}, ]
    # return JsonResponse({
    #     'status':200,
    #     'data':data
    # })
    return render(request,'articles_list.html',{'article_list':article_list})

# 文章添加
@login_required
def articles_add(request):
    response = {'status':200,'error_msg':''}
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        user_id = request.POST.get('user_id')
        if not title:
            response['error_msg'] = '标题不能为空'
            response['status'] = 400
            return JsonResponse(response)
        if not content:
            response['error_msg'] = '标题不能为空'
            response['status'] = 400
            return JsonResponse(response)
        if not user_id:
            response['error_msg'] = '标题不能为空'
            response['status'] = 400
            return JsonResponse(response)

        Article.objects.create(title=title,content=content,user_id=user_id)
        print(response)
        return JsonResponse(response)

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


# 公告列表
def infomation_list(request):
    infomation = Info.objects.all()
    return render(request,'info_list.html',{'infomation':infomation})


# ########################################## 报装相关 ########################################


# 报装信息列表
@login_required
def reporting_list(request):
    reporting_all = Reporting.objects.all()
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
def repair_list(request):
    repair_all = TroubleShoot.objects.all()
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
            path = os.path.join(MEDIA_UPLOAD_IMGS,upload_img.name)
            response['url'] = 'http:127.0.0.1:8000/%s' % str(path)      # 返回url路径
        else:
            response['error'] = 1
            response['message'] = '上传失败'
    # print('返回信息',response)
    return JsonResponse(response)
