from django.db import models


class UserProfile(models.Model):
    """
    用户表
    """
    gender_choices = (
        (1, u'男'),
        (2, u'女')
    )
    building_choices = (
        (1,u'东照大厦1'),
        (2,u'东照大厦2')
    )
    floor_choices = (
        (1,u'一楼'),
        (2,u'二楼'),
        (3,u'三楼'),
        (4,u'四楼'),
    )
    role_choices = (
        (1,u'法人'),
        (2,u'财务'),
        (3,u'行政'),
        (4,u'其他'),
    )
    dpt_choices = (
        (1, u'法人'),
        (2, u'财务'),
        (3, u'行政'),
        (4, u'其他'),
    )
    uid = models.CharField(max_length=64,verbose_name='UID',null=True,blank=True)

    building = models.SmallIntegerField(choices=building_choices,default=1,verbose_name='大厦')
    floor = models.SmallIntegerField(choices=floor_choices,default=1,verbose_name='楼层')
    room = models.IntegerField(verbose_name='房号')
    company = models.CharField(max_length=64,verbose_name='公司名称')
    username = models.CharField(max_length=32, verbose_name='用户名')
    role = models.SmallIntegerField(choices=role_choices,default=1,verbose_name='所属角色')
    phone = models.CharField(max_length=32, verbose_name='手机')

    is_superuser = models.BooleanField(default=False,verbose_name='认证')

    createtime = models.DateTimeField(auto_now_add=True)
    department = models.SmallIntegerField(choices=dpt_choices,verbose_name='所属部门',null=True,blank=True)
    email = models.EmailField(max_length=32, verbose_name='邮件',null=True,blank=True)
    age = models.PositiveIntegerField(verbose_name='年龄',null=True,blank=True)
    gender = models.SmallIntegerField(choices=gender_choices, null=True, blank=True, verbose_name='性别')

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = '用户表'
    def __str__(self):
        return self.username

class SuperUser(models.Model):
    """关联用户"""
    company = models.CharField(max_length=64,verbose_name='公司名称')
    username = models.CharField(max_length=32, verbose_name='联系人')
    phone = models.CharField(max_length=32, verbose_name='联系人电话')

    weichat = models.CharField(max_length=32,null=True,blank=True,verbose_name='联系人微信')
    sid = models.CharField(max_length=64,verbose_name='UID',null=True,blank=True)

    class Meta:
        verbose_name = '关联认证表'
        verbose_name_plural = '关联用户表'
    def __str__(self):
        return '%s-%s' % (self.company,self.username)

class Article(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=32,verbose_name='标题')
    content = models.TextField(verbose_name="内容")
    createtime = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    summary = models.CharField(max_length=64,null=True,blank=True,verbose_name='简介')

    class Meta:
        verbose_name = '文章表'
        verbose_name_plural = '文章表'
    def __str__(self):
        return self.title

class Info(models.Model):
    """公告发布"""
    title = models.CharField(max_length=32, verbose_name='标题')
    content = models.TextField(verbose_name="内容")
    pulisher = models.CharField(max_length=32, verbose_name='发布人')
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")


    summary = models.CharField(max_length=64, null=True, blank=True, verbose_name='简介')

    class Meta:
        verbose_name = '公告表'
        verbose_name_plural = '公告表'

    def __str__(self):
        return self.title

class ReportingType(models.Model):
    """
    报装类型
    """
    type = models.CharField(max_length=32,verbose_name='报装类型')

    class Meta:
        verbose_name = '报装类型表'
        verbose_name_plural = '报装类型表'
    def __str__(self):
        return '%s' % self.type

class Reporting(models.Model):
    """
    报装申请
    """
    type = models.ForeignKey("ReportingType",on_delete=models.CASCADE,verbose_name="报装类型")
    user = models.CharField(max_length=32,verbose_name='报装人')
    remark = models.CharField(max_length=32,verbose_name='备注')
    createtime = models.DateTimeField(auto_now_add=True,null=True,blank=True,verbose_name="创建时间")

    status_choices = ((0,'未处理'),(1,'已处理'))
    status = models.SmallIntegerField(choices=status_choices,default=0,verbose_name="状态")

    class Meta:
        verbose_name = '报装申请表'
        verbose_name_plural = '报装申请表'
    def __str__(self):
        return '%s' % self.type


class TroubleType(models.Model):
    """
    故障类型
    """
    type = models.CharField(max_length=32, verbose_name='故障类型')

    class Meta:
        verbose_name = '故障类型表'
        verbose_name_plural = '故障类型表'
    def __str__(self):
        return  '%s' % self.type

class TroubleShoot(models.Model):
    """
    故障报修
    """
    type = models.ForeignKey("TroubleType", on_delete=models.CASCADE,verbose_name='报修类型')
    user = models.CharField(max_length=32,verbose_name='报装人')
    content = models.CharField(max_length=32, verbose_name='报修详情')
    img = models.ImageField(upload_to='./media/upload_imgs',verbose_name='图片')
    createtime = models.DateTimeField(auto_now_add=True,null=True, blank=True,verbose_name="创建时间")

    level_choice_type = ((0,'一般'),(0,'紧急'),(0,'较急'))
    level = models.SmallIntegerField(choices=level_choice_type,default=0,verbose_name='紧急程度')

    status_choices = ((0, '未处理'),  (1, '已处理'))
    status = models.SmallIntegerField(choices=status_choices, default=0,verbose_name="状态")

    class Meta:
        verbose_name = '故障报修表'
        verbose_name_plural = '故障报修表'
    def __str__(self):
        return '%s' % self.type