from django.http import JsonResponse, HttpResponseServerError, HttpResponseBadRequest, HttpResponseNotFound
from django.views import View
import json
import re
from backend.models import UserProfile,Reporting,TroubleShoot,Article

# 授权用户相关
class account_user(View):
    # 获取信息
    def get(self,request,*args,**kwargs):
        response = {'status':200,'msg':None}
        uid = request.GET('uid')
        if uid:
            user_obj = UserProfile.objects.filter(uid=uid).first()
            data={
                'username':user_obj.username,
                'phone':user_obj.phone,
                'email':user_obj.email,
                'company':user_obj.company,
                'department': user_obj.department
            }
            response['data'] = data
        else:
            response['status'] = 400
            response['msg'] = '没用找到该用户'
        return JsonResponse(response)

    # 用户授权
    def post(self,request,*args,**kwargs):
        try:
            userdata = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return HttpResponseBadRequest('请求的 JSON 无法解析')
        response = {}
        # print(userdata)
        building = userdata.get("building")
        floor = userdata.get("floor")
        room = userdata.get("room")
        company = userdata.get("company")
        username = userdata.get("username")
        role = userdata.get("role")
        phone = userdata.get("phone")


        if building and floor and room and company:
            UserProfile.objects.create(building=building,floor=floor,room=room,company=company,
                                       username=username,role=role,phone=phone)
            response['status'] = '201'
        else:
            response['status'] = '400',     # 失败
            response['msg'] = '用户授权失败',     # 失败
        return JsonResponse(response)

    # 用户个人资料修改
    def put(self,request,*args,**kwargs):
        response={}
        try:
            userdata = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return HttpResponseBadRequest('请求的 JSON 无法解析')
        uid = userdata.get("uid")
        username = userdata.get("username")
        phone = userdata.get("phone")
        company = userdata.get("company")
        email = userdata.get("email")
        department = userdata.get("department")
        if uid:
            UserProfile.objects.filter(uid=uid).update(username=username,phone=phone,
                                                       company=company,email=email,department=department)
            response['status'] = 200
            response['msg'] = "更新成功"
        else:
            response['status'] = 400
            response['msg'] = "找不到该用户"
        return JsonResponse(response)


class report(View):
    # 获取报装信息
    def get(self,request,*args,**kwargs):
        pass
    # 提交报装信息
    def post(self,request,*args,**kwargs):
        response = {}
        try:
            reportdata = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return HttpResponseBadRequest('请求的 JSON 无法解析')

        uid = reportdata.get("uid")
        type = reportdata.get("type")
        remark = reportdata.get("remark")

        if uid:
            user_obj = UserProfile.objects.filter(uid=uid).first()
            Reporting.objects.create(type=type,remark=remark,user_id=user_obj.id)
            response['status'] = 201
            response['msg'] = '提交成功'
        else:
            response['status'] = 400
            response['msg'] = '提交失败'
        return JsonResponse(response)

########################################################## 图片问题###########
class repair(View):
    # 获取报修信息
    def get(self,request,*args,**kwargs):
        response = {}
        try:
            reportdata = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return HttpResponseBadRequest('请求的 JSON 无法解析')
        uid = reportdata.get("uid")
        if uid:
            user_obj = UserProfile.objects.filter(uid=uid).first()          # 用户
            all_report = Reporting.objects.filter(user=user_obj).all()
            if all_report:
                data = []
                for report in all_report:
                    tmp = {}
                    tmp['type'] = report.type_id
                    tmp['remark'] = report.remark
                    tmp['status'] = report.status
                    data.append(tmp)
                response['status'] = 200
                response['data'] = data
            else:
                response['status'] = 200
                response['msg'] = '该用户没有报装信息'
        else:
            response['status'] = 400
            response['msg'] = '没有该用户'
            return JsonResponse(response)


    # 提交报修信息
    def post(self,request,*args,**kwargs):
        response = {}
        try:
            reportdata = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return HttpResponseBadRequest('请求的 JSON 无法解析')

        uid = reportdata.get("uid")

        type = reportdata.get("type")
        content = reportdata.get("content")
        img = reportdata.get("img")
        level = reportdata.get("level")

        if uid:
            user_obj = UserProfile.objects.filter(uid=uid).first()
            TroubleShoot.objects.create(type=type,content=content,level=level,user_id=user_obj.id)
            response['status'] = 201
            response['msg'] = '提交成功'
        else:
            response['status'] = 400
            response['msg'] = '提交失败'
        return JsonResponse(response)


def about(request):
    response = {}
    article_obj = Article.objects.all().first()
    if article_obj:
        data = {
            'title':article_obj.title,
            'content':article_obj.content,
        }
        print(article_obj.content)
        response['status'] = 200
        response['data'] = data
    return JsonResponse(response)