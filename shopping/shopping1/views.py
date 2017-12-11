from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import hashlib
from .models import UserInfo
# Create your views here.


# 用户主页
def index(request):
    name = request.session.get('uname', None)
    if name is None:
        context = {'style2': 'display:none'}
    else:
        context = {'title': '天天生鲜-主页', 'name': name, 'style1': 'display:none'}
    return render(request, 'shopping1/index.html', context)


# 用户注册
def register(request):
    return render(request, 'shopping1/register.html', {'title': '天天生鲜-用户注册'})


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


def login_out(request):
    del request.session['uname']
    return redirect('/index')
