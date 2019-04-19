# Generated by Django 2.1.8 on 2019-04-19 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_carousel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='backenduser',
            options={'permissions': (('user_manager', '用户管理'), ('article_manager', '文章管理'), ('info_manager', '公告管理'), ('reporting_manager', '报装管理'), ('repair_manager', '报修管理'), ('carousel_manager', '轮播管理')), 'verbose_name_plural': '后台管理员'},
        ),
    ]