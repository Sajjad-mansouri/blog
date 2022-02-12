from distutils.command.register import register
from django import template
from ..models import Category

register=template.Library()


@register.inclusion_tag("blog/partial/navbar.html")
def category_navbar():
    return {
        'category':Category.objects.activated()
    }
  


@register.inclusion_tag('account/partials/profile_link.html')
def active_link(request,link_name,content,classes):
    return {
        'request':request,
        'link_name':link_name,
        'link':f'account:{link_name}',
        'content':content,
        'classes':classes
    }