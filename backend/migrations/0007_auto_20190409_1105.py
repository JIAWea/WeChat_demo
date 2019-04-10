# Generated by Django 2.1.8 on 2019-04-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20190408_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='troubleshoot',
            options={'verbose_name': '故障报修表', 'verbose_name_plural': '故障报修表'},
        ),
        migrations.AlterField(
            model_name='reporting',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '未处理'), (1, '已处理')], default=0, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='troubleshoot',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '未处理'), (1, '已处理')], default=0, verbose_name='状态'),
        ),
    ]
