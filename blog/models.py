from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.template.defaultfilters import truncatechars
from  extension.utils import shamsi_converter
from account.models import User

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def activated(self):
        return self.filter(status=True)


class Category(models.Model):
    title=models.CharField(max_length=100,verbose_name='عنوان')
    slug=models.CharField(max_length=100,verbose_name='آدرس')
    parent=models.ForeignKey('self',default=None,null=True,blank=True,on_delete=models.SET_NULL,related_name='children',verbose_name='زیردسته')
    status=models.BooleanField(default=False,verbose_name='وضعیت')

    objects=CategoryManager()
    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'
        ordering=['parent__id']

    def __str__(self):
        return self.title

class Articles(models.Model):
    STATUS_CHOICE=(
        ('d','پیش نویس'),
        ('p','منتشر شده'),
        ('i','در حال بررسی'),
        ('b','برگشت خورده')
    
    )
    title=models.CharField(max_length=100,verbose_name='عنوان')
    slug=models.CharField(max_length=100,verbose_name='آدرس')
    category=models.ManyToManyField(Category,null=True,blank=True,related_name='articles',verbose_name='دسته بندی')
    image=models.ImageField(upload_to='article_image',verbose_name='عکس')
    author=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,verbose_name='نویسنده')
    description=models.TextField(verbose_name='متن مقاله')
    publish=models.DateTimeField(default=timezone.now,verbose_name='زمان انتشار')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    is_special=models.BooleanField(default=False,verbose_name='مقاله ویژه')
    status=models.CharField(max_length=1,choices=STATUS_CHOICE,verbose_name='وضعیت')
    objects=ArticleManager()
    class Meta:
        verbose_name='مقاله'
        verbose_name_plural='مقالات'
        ordering=['-publish']

    def thumbnail(self): #for use image in admin
        return format_html(f'<img  width=100 src="{self.image.url}">')

    thumbnail.short_description='عکس'


    def category_str_admin(self):  #manytomany don't show in admin panel
        return ' , '.join([cat.title for cat in self.category.all()])

    category_str_admin.short_description='دسته بندی'


    def description_admin(self):
        return truncatechars(self.description,150)

    description_admin.short_description='متن'

    def jpublish(self):
        return shamsi_converter(self.publish)

    def __str__(self):
        return self.title
