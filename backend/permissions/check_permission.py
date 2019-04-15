from django.shortcuts import render,redirect
from WeChatPM.settings import LOGIN_URL
from django.urls import resolve

def perm_check(perm,*args,**kwargs):
    """
    判断权限流程，通过django自带的has_perm()
    :param perm: 业务模块通过装饰器传过来的权限名称
    :param args: 接收request
    :param kwargs:
    :return:
    """
    # print(perm)                                   # 装饰器传入需要判断的权限名称 例如：backend.reporting_manager
    request = args[0]
    # resolve_url_obj = resolve(request.path)
    # current_url_name = resolve_url_obj.url_name     # 当前url的url_name
    # # print('---perm:', request.user, request.user.is_authenticated, current_url_name)

    if request.user.is_authenticated is False:
        return redirect(LOGIN_URL)
    if request.user.is_superuser:
        return True
    if request.user.has_perm(perm):
        print('当前用户%s有此权限' % request.user)
        return True
    else:
        print('当前用户%s有此权限' % request.user)
        return False


def check_permission(perm):
    """
    权限判断
    :param perm: 接收相应业务函数的权限名称，列如 backend.article_manager ，以此来判断用户使用拥有此权限
    :return:
    """
    def decor(func):
        def inner(*args,**kwargs):
            if not perm_check(perm,*args,**kwargs):     # 如果无权限，则返回403
                request = args[0]
                return render(request, '403.html')
            return func(*args,**kwargs)
        return inner
    return decor