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
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# 详细商品
class GoodsInfo(models.Model):
    class Meta:
        db_table = 'goods'
    name = models.CharField(max_length=30, blank=True,)
    prices = models.CharField(max_length=10, blank=True)
    unit = models.CharField(max_length=5, blank=True, default="500g")
    purchasetimes = models.CharField(max_length=10, default=0, null=True, blank=True)
    commenttimes = models.CharField(max_length=10, default=0, null=True, blank=True)
    clickvolume = models.CharField(max_length=10, default=0, null=True, blank=True)
    imageaddress = models.CharField(max_length=30, default=0, null=True, blank=True)
    type = models.ForeignKey(GoodsType)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
