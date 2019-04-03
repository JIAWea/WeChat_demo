from django.contrib import admin
from . import models

admin.site.register(models.UserProfile)
admin.site.register(models.Article)
admin.site.register(models.ReportingType)
admin.site.register(models.Reporting)
admin.site.register(models.TroubleType)
admin.site.register(models.TroubleShoot)


