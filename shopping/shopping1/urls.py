from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index$', views.index),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^login_handle/$', views.login_handle),
    url(r'^login_out/$', views.login_out),
    url(r'^user_center/$', views.user_center),
    url(r'^user_center_order/$', views.user_center_order),
    url(r'^user_center_site/$', views.user_center_site),
]
