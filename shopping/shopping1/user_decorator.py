from django.http import HttpResponseRedirect


# 点击立即购买或加入购物车的时候转到登陆界面，完成登录后返回之前的页面
def login(func):
    def login_fun(request, *args, **kwargs):
        if request.session.has_key('uname'):
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/login/')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_fun