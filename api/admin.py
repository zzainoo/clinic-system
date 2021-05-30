from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
admin.site.site_header='مختبر وقت بغداد'
admin.site.site_title='مختبر وقت بغداد'

class UsersAdmin(admin.ModelAdmin):
    fields = ['name','phone','address','bio','code']
    list_display = ['id','name','phone','address','bio']
    search_fields = ['name','phone','address']
    list_display_links = ['id','name']

class ReportsAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user','lib']
    search_fields = ['user','lib','name']
    list_display = ['id','user','lib','name','file']
    list_display_links = ['id','user']
    list_filter = ['data','lib']


class LibAdmin(admin.ModelAdmin):
    fields = ['name', 'phone', 'address', 'bio']
    list_display = ['id', 'name', 'phone', 'address', 'bio']
    search_fields = ['name', 'phone', 'address']
    list_display_links = ['id', 'name']


class OffersAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','date']
    list_display_links = ['id','title']
    search_fields = ['title','descrp']
    list_filter = ['date']

class RegAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','address','phone','gender']
    list_display_links = ['id','firstname']
    search_fields = ['firstname','lastname','phone','address']
    list_filter = ['date','gender']


class HouseAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','phone','date']
    list_display_links = ['id','name']
    list_filter = ['date']
    search_fields = ['name','phone']

class TrainAdmin(admin.ModelAdmin):
    list_display = ['id','name','school','grad','period','date']
    list_display_links = ['id','name']
    search_fields = ['name','school','grad']
    list_filter = ['date']

admin.site.unregister(Group)
#admin.site.unregister(Token)
admin.site.register(Users,UsersAdmin)
admin.site.register(Libs,LibAdmin)
admin.site.register(Reports,ReportsAdmin)
admin.site.register(Offer,OffersAdmin)
admin.site.register(Registers,RegAdmin)
admin.site.register(Housecheck,HouseAdmin)
admin.site.register(Train,TrainAdmin)