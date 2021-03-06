from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from backend.models import *
from django.http import JsonResponse
import json,os
import uuid
from backend.permissions.permissions import *
from backend.permissions.check_permission import check_permission
from django.views.decorators.csrf import csrf_exempt
from WeChatPM.settings import USER_UP_XLSX
from backend.xlsxHandler import xlsxHandler
from django.db.models import Q


# 后台用户登录
def ac_login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect(request.GET.get('next','/backend/index/'))
        else:
            return render(request,'login.html',{'error_msg':"用户名或密码错误!"})
    return render(request,'login.html')

# 后台用户退出
def ac_logout(request):
    """
    退出登录
    :param request:
    :return:
    """
    logout(request)
    return redirect('/login')

# 后台用户更改密码
@login_required
def chenge_password(request):
    """
    重设密码
    :param request:
    :return:
    """
    user = request.user
    # print(user)
    err_msg = ''
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '').strip()
        new_password = request.POST.get('new_password', '').strip()
        repeat_password = request.POST.get('repeat_password', '').strip()
        # print(old_password)
        # 检查旧密码是否正确
        if user.check_password(old_password):
            if not new_password:
                err_msg = '新密码不能为空'
            elif new_password != repeat_password:
                err_msg = '两次密码不一致'
                return JsonResponse({'err_msg': err_msg, })
            else:
                user.set_password(new_password)
                user.save()
            return redirect("/login/")
        else:
            err_msg = '原密码输入错误'
            return JsonResponse({'err_msg': err_msg,})

# 后台用户添加
def backenduser_add(request):
    user = request.user
    response = {}
    if request.method == "POST":
        if user.is_superuser:
            # print('body',request.body)                      # 字节
            content = str(request.body,encoding='utf-8')
            data = json.loads(content)                      # 转为字典类型

            username = data.get('username')
            password = data.get('password')
            repeat_password = data.get('repeat_password')
            permissions = data.get('permissions')

            if username and password and repeat_password:
                if password != repeat_password:
                    return JsonResponse({'err_msg':'密码不一致'})
                exist_user = BackendUser.objects.filter(name=username).first()
                if exist_user:
                    response['err_msg'] = '该用户已经存在，请选择另一个用户名'
                    return JsonResponse(response)

                BackendUser.objects.create_user(name=username,email='',password=password)
                response['err_msg'] = '添加成功'

                # 创建权限
                ret = change_permission(request, username, permissions)     # 成功返回True 否正返回False
                if not ret:
                    response['err_msg'] = '添加成功，权限分配失败'
                return JsonResponse(response)
            else:
                return JsonResponse({'err_msg':'用户名或密码不能为空'})
        else:
            return JsonResponse({'err_msg':'只有超级管理员才能添加管理员'})


#########################################################################################

# 普通用户列表
@login_required
@check_permission('backend.user_manager')
def users_list(request):
    users_all = UserProfile.objects.all().order_by('-id')
    if request.method == "POST":
        content = request.body                      # 字节
        content = str(content, encoding='utf-8')    # 字符串
        result = json.loads(content)
        # print('结果', result,type(result))               # {'value': 'True', 'postList': ['5']} <class 'dict'>
        response = {'status':False,'msg':None}
        # for id in result:
        for id in result['postList']:
            if id:
                obj = UserProfile.objects.filter(id=id).first()
                # if obj.is_superuser:
                #     response['msg'] = '该用户已经认证过了'
                # else:
                    # UserProfile.objects.filter(id=id).update(is_superuser=True)
                UserProfile.objects.filter(id=id).update(is_superuser=result['value'])
                response['status'] = True
                response['msg'] = '设置成功'
            else:
                response['msg'] = '设置失败'
        return JsonResponse(response)

    return render(request, 'users_list.html',{'users_all':users_all})

# 普通用户删除
@check_permission('backend.user_manager')
@login_required
def users_delete(request):
    if request.method == "POST":
        content = request.body  # 字节
        content = str(content, encoding='utf-8')  # 字符串
        result = json.loads(content)
        # print('结果', type(result))               # [1,2,3]
        response = {'status': False, 'msg': None}
        for id in result:
            if id:
                obj = UserProfile.objects.filter(id=id).first()
                if not obj:
                    response['msg'] = '该用户已经被删除过了'
                else:
                    UserProfile.objects.filter(id=id).delete()
                    response['status'] = True
                    response['msg'] = '删除成功'
            else:
                response['msg'] = '删除失败'
        return JsonResponse(response)


# 企业关联用户
@check_permission('backend.user_manager')
@login_required
def superusers_list(request):
    search_name = request.GET.get("q",'')
    superusers_all = SuperUser.objects.all().order_by('-id')
    if search_name:
        q = Q()
        q.connector = 'OR'      # 模糊查询，可以查公司名称或用户名
        q.children.append(('company__contains',search_name))
        q.children.append(('username__contains',search_name))
        superusers_all = superusers_all.filter(q)
    return render(request, 'superusers_list.html',{'superusers_all':superusers_all})

# 企业关联用户删除
@check_permission('backend.user_manager')
@login_required
def superusers_delete(request):
    if request.method == "POST":
        content = request.body  # 字节
        content = str(content, encoding='utf-8')  # 字符串
        result = json.loads(content)
        # print('结果', type(result))               # [1,2,3]
        response = {'status': False, 'msg': None}
        for id in result:
            if id:
                obj = SuperUser.objects.filter(id=id).first()
                if not obj:
                    response['msg'] = '该用户已经被删除过了'
                else:
                    SuperUser.objects.filter(id=id).delete()
                    response['status'] = True
                    response['msg'] = '删除成功'
            else:
                response['msg'] = '删除失败'
        return JsonResponse(response)

# 批量导入企业用户
@csrf_exempt
@check_permission('backend.user_manager')
@login_required
def superusers_blukadd(request):
    response = {'status':True}
    if request.method == "POST":
        # print(request.FILES)
        uploadedFile = request.FILES.get('file')
        # print(uploadedFile.size)      # 文件大小
        name,layout = uploadedFile.name.split(".")
        # print(name,layout)
        if uploadedFile.size > 1048576:     # 1048576字节 == 1M
            return JsonResponse({"status":False,"msg":"导入失败，文件大小不能超过1M"})
        elif layout != 'xlsx':
            return JsonResponse({"status":False,"msg":"导入失败，表格必须为xlsx格式"})

        if uploadedFile:
            # with open('C:\\Users\\admin\\Desktop\\100.xlsx', 'wb') as f:
            #     for line in uploadedFile.chunks():
            #         f.write(line)
            nid = str(uuid.uuid4())  # 生成随机数作为路径
            path_file = os.path.join(USER_UP_XLSX, nid + uploadedFile.name)
            with open(path_file, 'wb') as f:
                for line in uploadedFile.chunks():
                    f.write(line)                   # 保存到本地路径
            local_path = path_file
            print('local_path',local_path)
            ret = xlsxHandler(local_path)             # 写入数据库
            if ret == '导入成功':
                response['msg'] = '导入成功'
            else:
                response['status'] = False
                response['msg'] = ret
        else:
            return HttpResponse('无文件')
    return JsonResponse(response)