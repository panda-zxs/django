from django.db import models


# 用户信息
class UserInfo(models.Model):
    class Meta:
        db_table = 'userinfo'
    uname = models.CharField(max_length=40, null=False, blank=False)
    upwd = models.CharField(max_length=40, null=False, blank=False)
    ucretime = models.DateTimeField()
    uemail = models.CharField(max_length=40)
    utelephone = models.CharField(max_length=20, null=True, blank=True)
    uaddress = models.CharField(max_length=100, null=True, blank=True)
    uzipcode = models.CharField(max_length=6, null=True, blank=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.uname


# 收获地址
class UserShipping(models.Model):
    class Meta:
        db_table = 'usership'
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    address3 = models.CharField(max_length=100)
    address4 = models.CharField(max_length=100)
    address5 = models.CharField(max_length=100)
    address6 = models.CharField(max_length=100)
    name = models.ForeignKey(UserInfo)


# 收货人信息
class ShippingName(models.Model):
    class Meta:
        db_table = 'shipname'
    ushipname1 = models.CharField(max_length=20)
    ushipname2 = models.CharField(max_length=20)
    ushipname3 = models.CharField(max_length=20)
    ushipname4 = models.CharField(max_length=20)
    ushipname5 = models.CharField(max_length=20)
    ushipname6 = models.CharField(max_length=20)
    name = models.ForeignKey(UserInfo)


# 商品分类
class GoodsType(models.Model):
    class Meta:
        db_table = 'goodstype'
    name = models.CharField(max_length=40,)
    type = models.ForeignKey('self', null=True, blank=True,)
    typenumber = models.CharField(max_length=6, default=0000)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# 详细商品
class GoodsInfo(models.Model):
    class Meta:
        db_table = 'goods'
    name = models.CharField(max_length=30, blank=True,)
    prices = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=5, blank=True, default="500g")
    # 购买次数
    purchase = models.IntegerField(default=0)
    # 评论数
    commenttimes = models.IntegerField(default=0)
    # 点击量
    clickvolume = models.IntegerField(default=0)
    # 商品编号
    productnumber = models.CharField(max_length=10, default=0000)
    # 商品简介
    description = models.TextField(default=1)
    type = models.ForeignKey(GoodsType)
    isDelete = models.BooleanField(default=False)
    members = models.ManyToManyField(UserInfo, through='CartInfo', through_fields=('goodsinfo', 'userinfo'))

    def __str__(self):
        return self.name


# 购物车
class CartInfo(models.Model):
    class Meta:
        db_table = 'cartinfo'
    userinfo = models.ForeignKey(UserInfo)
    goodsinfo = models.ForeignKey(GoodsInfo)
    number = models.IntegerField(default=0)

