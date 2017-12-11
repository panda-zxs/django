from django.db import models

# Create your models here.


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


class UserShipping(models.Model):
    class Meta:
        db_table = 'usership'
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    address3 = models.CharField(max_length=100)
    address4 = models.CharField(max_length=100)
    address5 = models.CharField(max_length=100)
    address6 = models.CharField(max_length=100)


class ShippingName(models.Model):
    class Meta:
        db_table = 'shipname'
    ushipname1 = models.CharField(max_length=20)
    ushipname2 = models.CharField(max_length=20)
    ushipname3 = models.CharField(max_length=20)
    ushipname4 = models.CharField(max_length=20)
    ushipname5 = models.CharField(max_length=20)
    ushipname6 = models.CharField(max_length=20)
