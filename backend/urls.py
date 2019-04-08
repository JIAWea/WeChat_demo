from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from backend.views import acount
from backend.views import home

urlpatterns = [

    # 文章相关
    url(r'articles$',home.articles_list,name='articles_list'),
    url(r'articles/add$',home.articles_add,name='articles_add'),
    url(r'articles/edit/(?P<aid>(\d+))$',home.articles_edit),
    url(r'articles/delete/(?P<aid>(\d+))$',home.articles_delete),

    # 报装相关
    url(r'reporting$', home.reporting_list, name='reporting_list'),
    url(r'reporting/add$', home.reporting_add,name='reporting_add'),
    url(r'reporting/edit/(?P<rid>(\d+))$', home.reporting_edit),
    url(r'reporting/delete/(?P<rid>(\d+))$', home.reporting_delete),

    # 报修相关
    url(r'repair$' , home.repair_list , name='repair_list'),
    url(r'repair/add$', home.repair_add , name='repair_add'),

    # 文件上传
    url(r'zopen/img/upload',home.img_upload),

    # 主页
    url(r'',home.index,name='index'),

    # 轮播图


]
