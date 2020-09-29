from django.contrib import admin
from .models import EnableCenter


class EnableCenterAdmin(admin.ModelAdmin):
	list_display = ('name', 'mail', 'phone_num', 'address', 'business_hours')


admin.site.register(EnableCenter, EnableCenterAdmin)
