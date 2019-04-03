"""WeChatPM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from backend.views import acount
from backend.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'login$',acount.ac_login,name='login'),
    url(r'register$',acount.ac_register,name='register'),

    url(r'index$',home.index,name='index'),

    url(r'articles$',home.articles_list,name='articles_list'),
    url(r'articles/add$',home.articles_add,name='articles_add'),
    url(r'articles/edit/(?P<aid>(\d+))$',home.articles_edit),
    url(r'articles/delete/(?P<aid>(\d+))$',home.articles_delete),

    url(r'reporting$', home.reporting_list, name='reporting_list'),
    url(r'reporting/add$', home.reporting_add,name='reporting_add'),
    url(r'reporting/edit/(?P<rid>(\d+))$', home.reporting_edit),
    url(r'reporting/delete/(?P<rid>(\d+))$', home.reporting_delete),

]
