from django.urls import path

from .views import PostDetailView, PostListView, CreatePostCommentView, UpdatePostCommentView


app_name = "blog"

urlpatterns = [
    path('search/', PostListView.as_view(), name='post_list'),
    path('detial/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post-comment-create/', CreatePostCommentView.as_view(), name='create_post_comment'),
    path('post-comment-update/<int:pk>/', UpdatePostCommentView.as_view(), name='update_post_comment'),
    path('post-comment-delete/<int:pk>/', UpdatePostCommentView.as_view(), name='delete_post_comment'),
]
