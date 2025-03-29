from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.





class Image(models.Model):
    photo = models.ImageField(upload_to='images/%m-%Y/', verbose_name='تصویر')
    title = models.CharField(verbose_name='عنوان تصویر', max_length=100)
    publish = models.DateTimeField(auto_now=True, verbose_name='تاریخ')   
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name="imageup", verbose_name='ارسال کننده')
    def __str__(self):
        return self.title



class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, verbose_name='نام کاربری')
    def __str__(self):
        return self.username

