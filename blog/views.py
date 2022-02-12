from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from account.mixins import AuthorAccessMixin
from .models import Articles,Category

class ArticlesList(ListView):
    #context_object_name='articles'
    paginate_by=1
    template_name='blog/article_list.html'
    queryset=Articles.objects.published()


class ArticleDetail(DetailView):
    template_name='blog/article_detail.html'
    context_object_name='article'
    def get_object(self):
        slug=self.kwargs.get('slug')
        article=get_object_or_404(Articles.objects.published(),slug=slug)
        return article

class ArticlePreview(AuthorAccessMixin,DetailView):
    template_name='blog/article_detail.html'
    context_object_name='article'
    def get_object(self):
        pk=self.kwargs.get('pk')
        article=get_object_or_404(Articles,pk=pk)
        return article

class CategoryList(ListView):
    paginate_by=1
    template_name='blog/category_list.html'
    def get_queryset(self):
        global category
        slug=self.kwargs.get('slug')
        category=get_object_or_404(Category.objects.activated(),slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):

        context=super().get_context_data(**kwargs)
        context['category']=category
        return context
