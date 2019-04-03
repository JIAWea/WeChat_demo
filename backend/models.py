from django.db import models

class UserProfile(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=32,verbose_name='用户名')
    password = models.CharField(max_length=64, verbose_name='密码')

    gender_choices = ((1, u'男'), (2, u'女'))
    gender = models.SmallIntegerField(choices=gender_choices,default=1,verbose_name='性别')

    email = models.EmailField(max_length=32,verbose_name='邮件',null=True,blank=True)
    phone = models.CharField(max_length=32, verbose_name='手机',null=True,blank=True)
    age = models.PositiveIntegerField(verbose_name='年龄',null=True,blank=True)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = '用户表'
    def __str__(self):
        return self.username


class Article(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=32,verbose_name='标题')
    summary = models.CharField(max_length=64,null=True,blank=True,verbose_name='简介')
    content = models.TextField(verbose_name="内容")
    createtime = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    user = models.ForeignKey(to="UserProfile",on_delete=models.CASCADE,verbose_name="发布者")

    class Meta:
        verbose_name = '文章表'
        verbose_name_plural = '文章表'
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
    user = models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    remark = models.CharField(max_length=32,verbose_name='备注')
    createtime = models.DateTimeField(auto_now_add=True,null=True,blank=True,verbose_name="创建时间")

    status_choices = ((0,'未处理'),(1,'处理中'),(2,'已解决'))
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
    故障保修
    """
    type = models.ForeignKey("TroubleType", on_delete=models.CASCADE,verbose_name='报修类型')
    user = models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    content = models.CharField(max_length=32, verbose_name='报修详情')
    img = models.ImageField(upload_to='./media/upload_imgs',verbose_name='图片')
    createtime = models.DateTimeField(auto_now_add=True,null=True, blank=True,verbose_name="创建时间")

    level_choice_type = ((0,'一般'),(0,'紧急'),(0,'较急'))
    level = models.SmallIntegerField(choices=level_choice_type,default=0,verbose_name='紧急程度')

    status_choices = ((0, '未处理'), (1, '处理中'), (2, '已解决'))
    status = models.SmallIntegerField(choices=status_choices, default=0,verbose_name="状态")

    class Meta:
        verbose_name = '故障保修表'
        verbose_name_plural = '故障保修表'
    def __str__(self):
        return '%s' % self.type