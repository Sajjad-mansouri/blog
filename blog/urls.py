from django.urls import  path
from .views import ArticlesList,ArticleDetail,CategoryList,ArticlePreview


app_name='blog'
urlpatterns=[
    path('',ArticlesList.as_view(),name='articles'),
    path('article/<slug:slug>',ArticleDetail.as_view(),name='article_detail'),
    path('article-preview/<int:pk>',ArticlePreview.as_view(),name='article_preview'),
    path('category/<slug:slug>',CategoryList.as_view(),name='category')

]