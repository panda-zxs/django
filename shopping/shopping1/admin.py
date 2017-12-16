from django.contrib import admin
from .models import *
# Register your models here.


class GoodsInfoAdmin(admin.TabularInline):
    model = GoodsInfo
    extra = 0


class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [GoodsInfoAdmin]


class UserInfoAdmin(admin.TabularInline):
    model = UserInfo
    extra = 0


class CartInfoAdmin(admin.ModelAdmin):
    inlines = [GoodsInfoAdmin]
    inlines = [UserInfoAdmin]

admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(GoodsInfo)
admin.site.register(UserInfo)
admin.site.register(CartInfo)
