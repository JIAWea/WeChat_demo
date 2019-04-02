from django.shortcuts import render

# Create your views here.
def ac_login(request):
    """
    用户登录
    :param request:
    :return:
    """

    return render(request,'login.html')

def ac_register(request):
    """
    用户注册
    :param request:
    :return:
    """
    return render(request,'register.html')