from django.urls import path, include
from . import views
from .views import (PostListView, PostCreateView, PostProfileView, PostUpdateView, PostDeleteView)

#Rutiranje za posts aplikaciju
urlpatterns = [
    path('', PostListView.as_view(), name = 'posts-board'),
    path('new_post/', PostCreateView.as_view(), name = 'posts-new_post'),
    path('edit_post/<int:pk>/', PostUpdateView.as_view(), name = 'posts-edit_post'),
    path('delete_post/<int:pk>/', PostDeleteView.as_view(), name = 'posts-delete_post'),
]
