from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女"),
)


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    mobile = models.CharField(max_length=11, unique=True, verbose_name="手机号码")
    image = models.ImageField(upload_to="head_image/%Y/%m", verbose_name="头像", default="head_image/default.jpg")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username
