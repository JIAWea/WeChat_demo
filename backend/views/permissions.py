from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse
from django.contrib.auth.models import Permission
from backend import models


# 修改权限
@login_required
def change_permission(request,username,permissions):
    if request.user.is_superuser:
        # print('测试ing',username,permissions)
        permissionsList = [
            'user_manager',
            'article_manager',
            'info_manager',
            'reporting_manager',
            'repair_manager',
        ]

        permissions = permissions.split(', ')
        # print(permissions,type(permissions))

        if permissions[0] != '':   # 不为空时
            for index, value in enumerate(permissions):
                permissions[index] = permissionsList[int(value)]    # 将 数字 替换为 上面数组中的 字符串
            print(permissions)
        else:
            permissions = []

        changeResult = db_change_permission(username, permissions)
        return HttpResponse(changeResult)



# 修改权限
def db_change_permission(username, permissions):
    try:
        user = models.BackendUser.objects.get(name=username)
        print('用户',user)
        if user:
            if permissions:
                # print('有权限列表',permissions)
                pers = []
                for per in permissions:
                    db_per = Permission.objects.filter(codename=per).values('id')[0]['id']   # 只把 id 取出来
                    print('db_per-------',db_per)
                    pers.append(db_per)
                #print(pers)   # 形如： [147, 150, 152]  数字为 auth_permission 中的 id
                print('pers列表',pers)
                # user.user_permissions = pers  # 这里，只能 加 id，加 codename 是不行的！！！
                user.user_permissions.set(pers)  # 这里，只能 加 id，加 codename 是不行的！！！
                print('设置完的用户权限')
            else:
                user.user_permissions.clear()
            models.BackendUser.objects.get(name=username)   # 刷新 缓存
            # print('用户权限',user.get_all_permissions())
        else:
            return '没有此用户'
    except Exception:
        return False
    else:
        return True    # 修改成功
