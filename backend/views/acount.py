from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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
            return redirect(request.GET.get('next','/index'))
        else:
            return render(request,'login.html',{'error_msg':"用户名或密码错误!"})
    return render(request,'login.html')


def ac_logout(request):
    """
    退出登录
    :param request:
    :return:
    """
    logout(request)
    return redirect('/login')


def ac_register(request):
    """
    用户注册
    :param request:
    :return:
    """
    return render(request,'register.html')


#
# @login_required
# def set_password(request):
#     """
#     重设密码
#     :param request:
#     :return:
#     """
#     user = request.user
#     err_msg = ''
#     if request.method == 'POST':
#         old_password = request.POST.get('old_password', '')
#         new_password = request.POST.get('new_password', '')
#         repeat_password = request.POST.get('repeat_password', '')
#         # 检查旧密码是否正确
#         if user.check_password(old_password):
#             if not new_password:err_msg = '新密码不能为空'
#             elif new_password != repeat_password:
#                 err_msg = '两次密码不一致'
#             else:
#                 user.set_password(new_password).save()
#             return redirect("/login/")
#         else:
#             err_msg = '原密码输入错误'
#             content = {'err_msg': err_msg,}
#             return render(request, 'set_password.html', content)