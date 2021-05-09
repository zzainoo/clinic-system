from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
admin.site.site_header='مختبر وقت بغداد'
admin.site.site_title='مختبر وقت بغداد'


class ReportsAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user','lib']

class UserAdmin(admin.ModelAdmin):
    search_fields = ['name']

class LibAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.unregister(Group)
#admin.site.unregister(Token)
admin.site.register(Users,UserAdmin)
admin.site.register(Libs,LibAdmin)
admin.site.register(Reports,ReportsAdmin)
admin.site.register(Offer)
admin.site.register(Registers)
