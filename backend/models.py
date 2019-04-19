from django.db import models
from django.contrib.auth.models import Permission,ContentType



from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)

class BackendUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not name:
            raise ValueError('Users must have an name')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

# 自定制admin后台管理员
class BackendUser(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=64, verbose_name="用户名",unique=True)
    email = models.EmailField(
        verbose_name='邮件',
        max_length=255,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)         # 决定是否可以登录后台
    is_staff = models.BooleanField(default=True)          # 决定是否可以登录后台

    objects = BackendUserManager()
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        # The user is identified by their email address
        return self.name

    def get_short_name(self):
        # The user is identified by their email address
        return self.name

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "后台管理员"
        permissions = (
            ('user_manager','用户管理'),
            ('article_manager','文章管理'),
            ('info_manager','公告管理'),
            ('reporting_manager','报装管理'),
            ('repair_manager','报修管理'),
            ('carousel_manager','轮播管理'),
        )




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
    user = models.ForeignKey("UserProfile",on_delete=models.CASCADE,verbose_name="报装人")
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
    user = models.ForeignKey("UserProfile",on_delete=models.CASCADE,verbose_name="报修人")
    content = models.CharField(max_length=32, verbose_name='报修详情')
    img = models.CharField(max_length=64,verbose_name='图片')
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


class Carousel(models.Model):
    caption = models.CharField(max_length=32,verbose_name="图片描述")
    path = models.CharField(max_length=64,verbose_name="图片路径")
    createtime = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="创建时间")