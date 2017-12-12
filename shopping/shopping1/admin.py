from django.contrib import admin
from .models import *
# Register your models here.


class GoodsInfoAdmin(admin.TabularInline):
    model = GoodsInfo
    extra = 5


class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [GoodsInfoAdmin]


admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(GoodsInfo)
