# Generated by Django 2.1.8 on 2019-04-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_auto_20190416_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='图片描述')),
                ('path', models.CharField(max_length=64, verbose_name='图片路径')),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
            ],
        ),
    ]
