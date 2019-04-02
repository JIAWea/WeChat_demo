from django.db import models

class UserProfile(models.Model):
    """
    用户表
    """
    gender_choices = ((1,u'男'),(2,u'女'))
    username = models.CharField(max_length=32,verbose_name='用户名')
    password = models.CharField(max_length=64, verbose_name='密码')
    email = models.EmailField(max_length=32,verbose_name='邮件')
    gender = models.SmallIntegerField(choices=gender_choices,default=1,verbose_name='性别')
    age = models.PositiveIntegerField(verbose_name='年龄')

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
    content = models.TextField(verbose_name="内容")
    user = models.ForeignKey(to="UserProfile",on_delete=models.CASCADE,verbose_name="发布者")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name = '文章表'
        verbose_name_plural = '文章表'
    def __str__(self):
        return self.title
