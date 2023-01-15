from django.urls import path
from .views import *
urlpatterns = [
    path('',index_view,name='index_url'),
    path('search/', search_view, name='search_url'),
    path('blog/<int:pk>/', blog_view, name='blog_url'),
    path('region/<int:pk>/', region_view, name='region_url'),
    path('blog_detail_view/<int:pk>/', blog_detail_view, name='blog_detail_url'),
    path('create_comment/<int:pk>/', create_comment, name='create_comment_url'),
    path('reply_comment/<int:pk>/', reply_comment, name='reply_comment_url'),
]