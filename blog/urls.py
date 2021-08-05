from django.urls import path
from .views import main_page, create_post,\
    user_posts, category_posts

urlpatterns = [
    path('category/<int:pk>/',category_posts, name='category_posts'),
    path('my-posts/', user_posts, name='my_posts'),
    path('create_post', create_post, name='create_post'),
    path('', main_page, name='main_page')
]


