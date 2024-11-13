from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDeleteAPIView, CommentListCreatAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='list-create-post'),
    path('posts/<int:id>/', PostRetrieveUpdateDeleteAPIView.as_view()),
    path('posts/<int:post_id>/comments/', CommentListCreatAPIView.as_view())

]