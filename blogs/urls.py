from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('post_unique/<int:id>', views.post_unique, name='post_unique'),
    path('search', views.search, name='search'),
]
