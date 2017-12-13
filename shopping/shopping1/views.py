from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import hashlib
from .models import *
from django.core.paginator import *
# Create your views here.


# 用户主页
# (商品多的话可以使用ajax异步加载，通过滚动条的位置判断是否要加载)
def index(request):
    type = GoodsType.objects.filter(typenumber__iregex=r'^[0-9]{1}$').order_by('typenumber')
    name = request.session.get('uname', None)
    if name is None:
        context = {'title': '天天生鲜-主页', 'style2': 'display:none'}
    else:
        context = {'title': '天天生鲜-主页', 'name': name, 'style1': 'display:none'}
    context.update({'type': type})
    return render(request, 'shopping1/index.html', context)


# 用户注册
def register(request):
    return render(request, 'shopping1/register.html', {'title': '天天生鲜-用户注册'})


# 用户注册逻辑
def register_handle(request):

    import time
    name = request.POST['user_name'] + 'abc'
    login_name = hashlib.md5(name.encode('utf-8')).hexdigest()
    pwd = request.POST['pwd'] + 'abc'
    login_pwd = hashlib.md5(pwd.encode('utf-8')).hexdigest()
    email = request.POST['email'] + 'abc'
    login_email = hashlib.md5(email.encode('utf-8')).hexdigest()
    time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if not UserInfo.objects.filter(uname=login_name):
        UserInfo.objects.create(uname=login_name, upwd=login_pwd, ucretime=time, uemail=login_email)
        return render(request, 'shopping1/register.html', {'js': '<script>alert("注册成功")</script>'})
    else:
        return render(request, 'shopping1/register.html', {'js': '<script>alert("用户名已存在")</script>'})


# 用户登录
def login(request):
    name = request.session.get('uname', '')
    if name is '':
        context = {'title': '天天生鲜-用户登录', 'name': '', 'check': ''}
    else:
        context = {'title': '天天生鲜-用户登录', 'name': name, 'check': 'checked'}
    return render(request, 'shopping1/login.html', context)


# 用户登录逻辑判断
def login_handle(request):
    name = request.POST['username'] + 'abc'
    pwd = request.POST['pwd'] + 'abc'
    hname = hashlib.md5(name.encode('utf-8')).hexdigest()
    hped = hashlib.md5(pwd.encode('utf-8')).hexdigest()
    if not UserInfo.objects.filter(uname=hname):
        return HttpResponse('无此用户')
    elif not UserInfo.objects.filter(upwd=hped):
        return HttpResponse('错误密码')
    else:
        request.session['uname'] = request.POST['username']
        print(request.POST.get('check', None))
        if request.POST.get('check', None) is None:
            request.session.set_expiry(0)
        else:
            request.session.set_expiry(None)
        return redirect('/index')


# 注销用户逻辑
def login_out(request):
    del request.session['uname']
    return redirect('/index')


# 用户中心页面
def user_center(request):
    name = request.session.get('uname', None)
    if name is None:
        context = {'title': '天天生鲜-用户中心', 'style2': 'display:none'}
    else:
        context = {'title': '天天生鲜-用户中心', 'name': name, 'style1': 'display:none'}
    return render(request, 'shopping1/user/user_center_info.html', context)


# 商品列表
def goods_list(request, id, index):
    types = GoodsType.objects.filter(typenumber__iregex=r'^[0-9]{1}$').order_by('typenumber')
    c = GoodsType.objects.get(typenumber=id)
    a = GoodsInfo.objects.filter(productnumber__startswith=id)
    b = GoodsInfo.objects.filter(productnumber__startswith='1')
    recommend = {'recommend1': b.get(name='柠檬'), 'recommend2': b.get(name='玫瑰香葡萄')}
    name = request.session.get('uname', None)
    if name is None:
        context = {'list': c, 'title': '天天生鲜-用户中心', 'style2': 'display:none'}
    else:
        context = {'list': c, 'title': '天天生鲜-用户中心', 'name': name, 'style1': 'display:none'}
    context.update(recommend)
    p = Paginator(a, 10)
    page = p.page(int(index))
    context.update({'page': page, 'id': id, 'types': types})
    return render(request, 'shopping1/goods/list.html', context)


# 商品详细页

def goods_detail(request, id):
    types = GoodsType.objects.filter(typenumber__iregex=r'^[0-9]{1}$').order_by('typenumber')
    c = GoodsType.objects.get(typenumber=id[:1])
    a = GoodsInfo.objects.get(productnumber=id)
    a.clickvolume += 1
    a.save()
    b = GoodsInfo.objects.filter(productnumber__startswith='1')
    recommend = {'recommend1': b.get(name='柠檬'), 'recommend2': b.get(name='玫瑰香葡萄')}
    name = request.session.get('uname', None)
    if name is None:
        context = {'types': types, 'type': c, 'list': a, 'title': '天天生鲜-用户中心', 'style2': 'display:none'}
    else:
        context = {'types': types, 'type': c, 'list': a, 'title': '天天生鲜-用户中心', 'name': name, 'style1': 'display:none'}
    context.update(recommend)
    return render(request, 'shopping1/goods/detail.html', context)
