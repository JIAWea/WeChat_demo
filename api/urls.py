from django.conf.urls import url
from api.views import account
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [

    url(r'account/user/$', account.account_user.as_view()),
    url(r'user/report/$', account.report.as_view()),
    url(r'user/repair/$', account.repair.as_view()),
    url(r'about/$', account.about),

]
