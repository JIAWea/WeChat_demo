from django.conf.urls import url,include
from backend.views import home
from backend.views import acount


urlpatterns = [

    # 文章相关
    url(r'articles/$',home.articles_list,name='articles_list'),
    url(r'article/add/$',home.articles_add,name='article_add'),
    url(r'article/edit/(?P<aid>(\d+))/$',home.article_edit),
    url(r'article/delete/(?P<aid>(\d+))/$',home.article_delete),
    url(r'article/upload-img/',home.article_img),                          # 文章图片


    # 公告列表
    url(r'infomation/$',home.infomation_list,name='infomation_list'),
    url(r'infomation/add/$',home.infomation_add,name='infomation_add'),
    url(r'infomation/delete/(?P<iid>(\d+))/$',home.infomation_delete),
    url(r'infomation/edit/(?P<iid>(\d+))/$',home.infomation_edit),
    url(r'infomation/upload-img/$',home.infomation_img),                # 公告图片

    # 报装相关
    url(r'reporting/$', home.reporting_list, name='reporting_list'),                # 列表
    url(r'reporting/delete/$', home.reporting_delete, name='reporting_delete'),     # 删除

    # 报修相关
    url(r'repair/$' , home.repair_list , name='repair_list'),                       # 列表
    url(r'repair/delete/$' , home.repair_delete , name='repair_delete'),            # 删除


    # 企业联系人用户的用户列表
    url(r'superusers/$',acount.superusers_list,name='superusers_list'),
    url(r'superusers/delete/$',acount.superusers_delete,name='superusers_delete'),

    # 所有关注小程序的用户列表
    url(r'users/$',acount.users_list,name='users_list'),
    url(r'users/delete/$',acount.users_delete,name='users_delete'),

    # 修改后台用户密码
    url(r'backenduser/change/password/$',acount.chenge_password),
    # 添加后台管理员
    url(r'backenduser/add/$',acount.backenduser_add),

    # 轮播图
    url(r'carousel/$',home.carousel_list,name='carousel_list'),
    url(r'carousel/add/$',home.carousel_add,name='carousel_add'),
    url(r'carousel/delete/(?P<cid>(\d+))/$',home.carousel_delete),
    # url(r'carousel/edit/(?P<cid>(\d+))/$',home.carousel_edit),

    # 无权限
    url(r'permissiondenied/$',home.permission_denied),
    # 主页
    url(r'index/',home.index,name='index'),




]
