from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^login_handle/$', views.login_handle),
    url(r'^login_out/$', views.login_out),
    url(r'^user_center/$', views.user_center),
    url(r'^goods/list/(?P<id>\w+)/(?P<index>\d*)/$', views.goods_list)
]
