from django.contrib import admin
from . import models
from django.contrib.auth.models import Permission

class AdminArticle(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'createtime')  # 指定要显示的字段
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
    list_display = ('id', 'content', 'img' , 'createtime', 'level' , 'status')  # 指定要显示的字段
    ordering = ('id',)



admin.site.register(models.UserProfile)
admin.site.register(models.Article)
admin.site.register(models.ReportingType,AdminReportingType)
admin.site.register(models.Reporting,AdminReporting)
admin.site.register(models.TroubleType,AdminTroubleType)
admin.site.register(models.TroubleShoot,AdminTroubleShoot)

admin.site.register(models.SuperUser)
admin.site.register(models.Info)

class BackendUserAdmin(admin.ModelAdmin):
    filter_horizontal = ('user_permissions', 'groups')
admin.site.register(models.BackendUser,BackendUserAdmin)


class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'codename')
    list_filter = ('content_type',)
admin.site.register(Permission,PermissionAdmin)

