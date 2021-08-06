from django.urls import path
from .views import (
    main_page, create_post,
    user_posts, category_posts, search, post_detail
)

urlpatterns = [
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('category/<int:pk>/', category_posts, name='category_posts'),
    path('my-posts/', user_posts, name='my_posts'),
    path('create_post', create_post, name='create_post'),
    path('search/', search, name='search'),
    path('', main_page, name='main_page'),
]


