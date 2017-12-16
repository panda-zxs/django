from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import hashlib
from .models import *
from django.core.paginator import *
from . import user_decorator

# Create your views here.


# 用户主页
# (商品多的话可以使用ajax异步加载，通过滚动条的位置判断是否要加载)
def index(request):
    type = GoodsType.objects.filter(typenumber__iregex=r'^[0-9]{1}$').order_by('typenumber')
    name = request.session.get('uname', None)
    number = len(CartInfo.objects.all())
    if name is None:
        context = {'title': '天天生鲜-主页', 'style2': 'display:none'}
    else:
        context = {'title': '天天生鲜-主页', 'name': name, 'style1': 'display:none'}
    context.update({'type': type, 'number': number})
    return render(request, 'shopping1/index.html', context)


# 用户注册
def register(request):
    return render(request, 'shopping1/register.html', {'title': '天天生鲜-用户注册'})


# 用户注册逻辑
def register_handle(request):

    import time
    login_name = request.POST['user_name']
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
    red = request.COOKIES.get('url', '/index')
    name = request.POST['username']
    pwd = request.POST['pwd'] + 'abc'
    hped = hashlib.md5(pwd.encode('utf-8')).hexdigest()
    if not UserInfo.objects.filter(uname=name):
        return HttpResponse('无此用户')
    elif not UserInfo.objects.filter(upwd=hped):
        return HttpResponse('错误密码')
    else:
        request.session['uname'] = name
        if request.POST.get('check', None) is None:
            request.session.set_expiry(0)
        else:
            request.session.set_expiry(None)
        return redirect(red)


# 注销用户逻辑
def login_out(request):
    del request.session['uname']
    return redirect('/index')


# 用户中心页面
@user_decorator.login
def user_center(request):
    goods_id = request.COOKIES.get('ids', '')
    ids = goods_id.split(',')
    goods_id = GoodsInfo.objects.filter(productnumber__in=ids)
    print(ids)
    name = request.session.get('uname', None)
    context = {'title': '用户中心', 'name': name, 'style1': 'display:none'}
    context.update({'goods_id': goods_id})
    return render(request, 'shopping1/user/user_center_info.html', context)


# 商品列表
@user_decorator.login
def goods_list(request, id, sort, index):
    types = GoodsType.objects.filter(typenumber__iregex=r'^[0-9]{1}$').order_by('typenumber')
    c = GoodsType.objects.get(typenumber=id)
    a = GoodsInfo.objects.filter(productnumber__startswith=id)
    number = len(CartInfo.objects.all())
    if sort == '1':
        s = a
    elif sort == '2':
        s = a.order_by('prices')
    else:
        s = a.order_by('clickvolume').reverse()
    # 商品推荐列表
    b = GoodsInfo.objects.filter(productnumber__startswith='1')
    recommend = {'recommend1': b.get(name='柠檬'), 'recommend2': b.get(name='玫瑰香葡萄')}
    name = request.session.get('uname', None)
    context = {'active': 'active', 'sort': sort, 'list': c, 'title': '天天生鲜-商品列表', 'name': name, 'style1': 'display:none'}
    context.update(recommend)
    p = Paginator(s, 10)
    page = p.page(int(index))
    context.update({'page': page, 'id': id, 'types': types, 'number': number})
    return render(request, 'shopping1/goods/list.html', context)


# 商品详细页
@user_decorator.login
def goods_detail(request, id):
    # 显示路径信息
    types = GoodsType.objects.filter(typenumber__iregex=r'^[0-9]{1}$').order_by('typenumber')
    # 储存点击量
    a = GoodsInfo.objects.get(productnumber=id)
    a.clickvolume += 1
    a.save()
    # 购物车数量
    number = len(CartInfo.objects.all())
    # 商品推荐列表
    b = GoodsInfo.objects.filter(productnumber__startswith='1')
    recommend = {'recommend1': b.get(name='柠檬'), 'recommend2': b.get(name='玫瑰香葡萄')}
    # 用户验证
    name = request.session.get('uname', None)
    context = {'number': number, 'types': types, 'list': a, 'title': '天天生鲜-商品详情', 'name': name, 'style1': 'display:none'}
    context.update(recommend)

    response = render(request, 'shopping1/goods/detail.html', context,)
    goods_id = request.COOKIES.get('ids', '')
    if goods_id != '':
        ids = goods_id.split(',')
        if id not in ids:
            ids.insert(0, id)
        if len(ids) > 5:
            ids.pop()
        goods_id = ','.join(ids)
    else:
        goods_id = str(id)
    response.set_cookie('ids', goods_id)
    return response


# 购物车
@user_decorator.login
def cart(request):

    # 用户验证
    name = request.session.get('uname', None)
    id = UserInfo.objects.get(uname=name).id
    list = CartInfo.objects.filter(userinfo_id=id)
    context = {'title': '购物车', 'name': name, 'style1': 'display:none', 'list': list}
    return render(request, 'shopping1/user/cart.html', context)


def cart_handle(request):
    num = request.GET['number']
    name = request.GET['name']
    user = request.session.get('uname')
    user_name = UserInfo.objects.get(uname=user)
    goods_name = GoodsInfo.objects.get(name=name)
    l = CartInfo.objects.filter(userinfo=user_name).filter(goodsinfo=goods_name)
    if len(l) == 0:
        CartInfo.objects.create(userinfo=user_name, goodsinfo=goods_name, number=num)
    else:
        for i in l:
            i.number = i.number+int(num)
            i.save()
    number = len(CartInfo.objects.all())
    ret = {'ret1': '添加成功', 'ret2': number}
    print(1)
    return JsonResponse(ret)


def cart_account(request):
    print(1)
    print(2)
    goods = request.GET['goods']

    list = []
    for i in goods:
        id = i['id']
        num = i['num']
        l = CartInfo.objects.get(id=id)
        l.number = num
        l.save()
        list.append(CartInfo.objects.get(id=id))
    context = {'list': list}
    return redirect('shopping1/user/place_order.html', context)
