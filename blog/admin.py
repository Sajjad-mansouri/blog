from django.contrib import admin
from .models import Articles,Category


class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','slug','parent','status']
    list_filter=['status']
    prepopulated_fields={'slug':('title',)}
    list_editable=['status']

admin.site.register(Category,CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','author','slug','category_str_admin','thumbnail','description_admin','publish','is_special','status']
    list_filter=['status','publish']
    prepopulated_fields={'slug':('title',)}
    list_editable=['status']

admin.site.register(Articles,ArticleAdmin)