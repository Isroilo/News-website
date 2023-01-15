from django.urls import path
from .views import *
urlpatterns = [
    path('create-blog',create_blog,name='create_blog_url'),
    path('users/', users_view, name='users_url'),
    path('user/detail/<int:pk>/', user_detail, name='user_detail_url'),
    path('user/update/<int:pk>/', user_update, name='user_update_url'),
    path('user/delete/<int:pk>/', user_delete, name='user_delete_url'),
    path('update_blog/<int:pk>/', update_blog, name='update_blog_url'),
    path('delete_blog/<int:pk>/', delete_blog, name='delete_blog_url'),
    path('search-user/', search_user_view, name='search_user_url'),
]