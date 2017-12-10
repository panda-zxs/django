from django.db import models

# Create your models here.


class UserInfo(models.Model):
    class Meta:
        db_table = 'userinfo'
    uname = models.CharField(max_length=40, null=False, blank=False)
    upwd = models.CharField(max_length=40, null=False, blank=False)
    ucretime = models.DateTimeField()
    uemail = models.CharField(max_length=40)
    isDelete = models.BooleanField(default=False)

