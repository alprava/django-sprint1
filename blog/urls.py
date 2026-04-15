from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(path('posts/<int:id>/', views.detail, name='post_detail'),
    path(
        'post/<int:id>/',
        views.detail,
        name='detail'),
    path(
        'category/<slug:category_slug>/',
        views.category_posts,
        name='category_posts'),
]
