from django.contrib import admin
from . import models

class AdminArticle(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'createtime','user_id')  # 指定要显示的字段
    ordering = ('id',)
    search_fields = ('title',)

class AdminUserProfile(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    ordering = ('id',)
    search_fields = ('username',)

class AdminReportingType(admin.ModelAdmin):
    list_display = ('id', 'type')
    ordering = ('id',)
    search_fields = ('type',)

class AdminReporting(admin.ModelAdmin):
    list_display = ('id', 'remark', 'createtime', 'user', 'status')  # 指定要显示的字段
    ordering = ('id',)


class AdminTroubleType(admin.ModelAdmin):
    list_display = ('id', 'type')
    ordering = ('id',)
    search_fields = ('type',)

class AdminTroubleShoot(admin.ModelAdmin):
    list_display = ('id', 'content', 'img' , 'createtime', 'user', 'level' , 'status')  # 指定要显示的字段
    ordering = ('id',)



admin.site.register(models.UserProfile,AdminUserProfile)
admin.site.register(models.Article,AdminArticle)
admin.site.register(models.ReportingType,AdminReportingType)
admin.site.register(models.Reporting,AdminReporting)
admin.site.register(models.TroubleType,AdminTroubleType)
admin.site.register(models.TroubleShoot,AdminTroubleShoot)


