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
    url(r'^goods/list/(?P<id>\d+)/(?P<sort>\d+)_(?P<index>\d+)/$', views.goods_list),
    url(r'^goods/detail/(\d+)$', views.goods_detail),
    url(r'^cart/$', views.cart),
    url(r'^cart_handle/$', views.cart_handle),
    url(r'^cart_account/$', views.cart_account),
    url(r'^cart_order/$', views.cart_order),
    url(r'^cart_del/$', views.cart_del),
]
