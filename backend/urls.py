from django.conf.urls import url,include
from backend.views import home
from backend.views import acount
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    # 文章相关
    url(r'articles/$',home.articles_list,name='articles_list'),
    url(r'articles/add/$',home.articles_add,name='articles_add'),
    url(r'articles/edit/(?P<aid>(\d+))/$',home.articles_edit),
    url(r'articles/delete/(?P<aid>(\d+))/$',home.articles_delete),

    # 报装相关
    url(r'reporting/$', home.reporting_list, name='reporting_list'),     # 列表
    url(r'reporting/delete/$', home.reporting_delete, name='reporting_delete'),     # 列表

    # 报修相关
    url(r'repair/$' , home.repair_list , name='repair_list'),            # 列表
    url(r'repair/delete/$' , home.repair_delete , name='repair_delete'),            # 列表


    # 文件上传
    url(r'zopen/img/upload',home.img_upload),

    # 企业联系人用户的用户列表
    url(r'superusers/$',acount.superusers_list,name='superusers_list'),
    url(r'superusers/delete/$',acount.superusers_delete,name='superusers_delete'),

    # 所有关注小程序的用户列表
    url(r'users/$',acount.users_list,name='users_list'),
    url(r'users/delete/$',acount.users_delete,name='users_delete'),

    # 公告列表
    url(r'infomation/$',home.infomation_list,name='infomation_list'),

    # 主页
    url(r'',home.index,name='index'),




]
