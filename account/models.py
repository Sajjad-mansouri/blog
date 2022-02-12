from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_author=models.BooleanField(default=False,verbose_name='وضعیت نویسندگی')
    special_user=models.DateTimeField(default=timezone.now,verbose_name='اشتراک ویژه تا')
    profile_image=models.ImageField(upload_to='profile_image',null=True,blank=True,verbose_name='عکس پروفایل')

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False

    is_special_user.boolean=True
    is_special_user.short_description='کاربر ویژه'
