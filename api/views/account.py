from django.http import JsonResponse, HttpResponseServerError, HttpResponseBadRequest, HttpResponseNotFound
from django.views import View
from WeChatPM.settings import STATIC_REPAIR_IMG,STATIC_URL
from backend.models import UserProfile,Reporting,TroubleShoot,Article,Info,Carousel
from django.views.decorators.csrf import csrf_exempt    # 局部屏蔽csrf
import os
import json

# 授权用户相关
class account_user(View):
    # 获取信息
    def get(self,request,*args,**kwargs):
        response = {'status':200,'msg':None}
        uid = request.GET.get('uid','')

        print(uid)
        user_obj = UserProfile.objects.filter(uid=uid).first()
        if user_obj:
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
        # try:
        #     userdata = json.loads(request.body.decode('utf-8'))
        # except ValueError:
        #     return HttpResponseBadRequest('请求的 JSON 无法解析')
        userdata = request.POST
        response = {}
        # print(userdata)
        uid = userdata.get("uid",'')

        building = userdata.get("building")
        floor = userdata.get("floor")
        room = userdata.get("room")
        company = userdata.get("company")
        username = userdata.get("username")
        role = userdata.get("role")
        phone = userdata.get("phone")

        if uid:
            if building and floor and room and company:
                UserProfile.objects.create(uid=uid,building=building,floor=floor,room=room,company=company,
                                           username=username,role=role,phone=phone)
                response['status'] = 200
                response['msg'] = '用户授权成功',  # 成功
            else:
                response['status'] = 400,     # 失败
                response['msg'] = '用户授权失败，请完善用户信息',     # 失败
        else:
            response['status'] = 400,  # 失败
            response['msg'] = '用户授权失败，识别不到用户唯一标识',   # 失败
        return JsonResponse(response)

    # 用户个人资料修改
    def put(self,request,*args,**kwargs):
        response={}
        # try:
        #     userdata = json.loads(request.body.decode('utf-8'))
        # except ValueError:
        #     return HttpResponseBadRequest('请求的 JSON 无法解析')
        userdata = request.POST

        uid = userdata.get("uid",'')

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

# 报装相关
class report(View):
    # 获取报装信息
    def get(self,request,*args,**kwargs):
        response = {'status': None, 'data': None, 'msg': None}
        uid = request.GET.get('uid','')
        user_obj = UserProfile.objects.filter(uid=uid).first()
        if user_obj:
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
                response['msg'] = '获取成功'
            else:
                response['status'] = 200
                response['data'] = ''
                response['msg'] = '该用户没有报装信息'
        else:
            response['status'] = 400
            response['msg'] = '没用找到该用户'
        return JsonResponse(response)

    # 提交报装信息
    def post(self,request,*args,**kwargs):
        response = {}
        # try:
        #     reportdata = json.loads(request.body.decode('utf-8'))
        # except ValueError:
        #     return HttpResponseBadRequest('请求的 JSON 无法解析')

        reportdata = request.POST
        uid = reportdata.get("uid",'')
        type = reportdata.get("type")
        remark = reportdata.get("remark")


        user_obj = UserProfile.objects.filter(uid=uid).first()
        if user_obj:
            Reporting.objects.create(type=type,remark=remark,user_id=user_obj.id)
            response['status'] = 200
            response['msg'] = '提交成功'
        else:
            response['status'] = 400
            response['msg'] = '提交失败，找不到该用户'
        return JsonResponse(response)

# 报修相关
class repair(View):
    # 获取报修信息                            #############################未完
    def get(self,request,*args,**kwargs):
        response = {'status':None,'data':None,'msg':None}
        uid = request.GET.get('uid','')

        user_obj = UserProfile.objects.filter(uid=uid).first()          # 用户
        if user_obj:
            all_repair = TroubleShoot.objects.filter(user=user_obj).all()
            if all_repair:
                data = []
                for repair in all_repair:
                    tmp = {}
                    tmp['type'] = repair.type
                    tmp['content'] = repair.content
                    tmp['img'] = repair.img
                    tmp['level'] = repair.level
                    tmp['status'] = repair.status
                    data.append(tmp)
                response['status'] = 200
                response['data'] = data
            else:
                response['status'] = 200
                response['data'] = ''
                response['msg'] = '该用户没有报修信息'
        else:
            response['status'] = 400
            response['msg'] = '没有该用户'
            return JsonResponse(response)


    # 提交报修信息
    def post(self,request,*args,**kwargs):
        response = {}
        # try:
        #     repairdata = json.loads(request.body.decode('utf-8'))
        # except ValueError:
        #     return HttpResponseBadRequest('请求的 JSON 无法解析')

        repairdata = request.POST
        uid = repairdata.get("uid",'')

        type = repairdata.get("type")
        content = repairdata.get("content")
        img = repairdata.get("img")
        level = repairdata.get("level")


        user_obj = UserProfile.objects.filter(uid=uid).first()
        if user_obj:
            TroubleShoot.objects.create(type=type,content=content,img=img,level=level,user_id=user_obj.id)
            response['status'] = 200
            response['msg'] = '提交成功'
        else:
            response['status'] = 400
            response['msg'] = '提交失败,找不到该用户'
        return JsonResponse(response)


# 报修图片上传
@csrf_exempt
def repair_img(request):
    response = {'error':0,'url':None,'message':'上传成功'}
    if request.method == "POST":
        upload_img = request.FILES.get('uploadImg')
        if upload_img:
            with open(os.path.join(STATIC_REPAIR_IMG,upload_img.name),'wb') as f:
                for line in upload_img.chunks():
                    f.write(line)
            path = os.path.join(STATIC_URL,'uploadImgs/repair/%s') % upload_img.name
            response['url'] = str(path)                      # 返回url路径
            # response['url'] = '/static/uploadImgs/repair/img名称’      # 返回url路径
        else:
            response['error'] = 1
            response['message'] = '上传失败'
    # print('返回信息',response)
    return JsonResponse(response)



# 关于我们
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

# 公告
def infomation(request):
    response = {'status':200,'msg':None,'data':None}
    all_info = Info.objects.all()
    data = []
    if all_info:
        for info in all_info:
            tmp = {}
            tmp['title'] = info.title
            tmp['content'] = info.content
            tmp['createtime'] = '%s-%s-%s' % (info.createtime.year,info.createtime.month,info.createtime.day)
            tmp['pulisher'] = info.pulisher
            data.append(tmp)
        response['data'] = data
        response['msg'] = "获取成功"
    else:
        response['data'] = ""
        response['msg'] = "获取成功,暂时无公告信息"
    return JsonResponse(response)

# 轮播图
def carousel(request):
    response = {'status': 200, 'msg': None, 'data': None}
    all_carousel = Carousel.objects.all()
    data = []
    if all_carousel:
        for carousel in all_carousel:
            tmp = {}
            tmp['caption'] = carousel.caption
            tmp['path'] = carousel.path
            data.append(tmp)
        response['data'] = data
        response['msg'] = "获取成功"
    else:
        response['data'] = ""
        response['msg'] = "获取成功,暂时无图片"
    return JsonResponse(response)