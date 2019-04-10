# Generated by Django 2.1.8 on 2019-04-10 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20190410_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='floor',
            field=models.SmallIntegerField(choices=[(1, '一楼'), (2, '二楼'), (3, '三楼'), (4, '四楼')], default=1, verbose_name='楼层'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_superuser',
            field=models.BooleanField(choices=[(1, '否'), (2, '是')], default=1, verbose_name='认证'),
        ),
    ]