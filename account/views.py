from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .mixins import FieldMixin,FormValidMixin,AuthorAccessMixin ,SuperuserAccessMixin
from .models import User
from blog.models import Articles
# Create your views here.
class ArticleList(LoginRequiredMixin,ListView):
    template_name='account/home.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Articles.objects.all()
        
        else:
            return Articles.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin,FieldMixin,FormValidMixin,CreateView):
    model=Articles
    
    template_name='account/article_create_update.html'
    success_url=reverse_lazy('account:home')

class ArticleUpdate(AuthorAccessMixin,FieldMixin,FormValidMixin,UpdateView):
    model=Articles
    template_name='account/article_create_update.html'
    success_url=reverse_lazy('account:home')

class ArticleDelete(SuperuserAccessMixin,DeleteView):
    model=Articles
    template_name='account/article_confirm_delete.html'
    success_url=reverse_lazy('account:home')

class Profile(UpdateView):
    model=User
    template_name='registration/profile.html'
    success_url=reverse_lazy('account:home')
    fields=['username','email','first_name','last_name','profile_image','special_user','is_author']

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
