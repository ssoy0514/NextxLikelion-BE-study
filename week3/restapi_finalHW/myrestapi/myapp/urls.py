from django.urls import path
from .views import PostAPIView,PostDetails,CommentAPIView, CommentAPIDetails

urlpatterns = [
    path('post_article/',PostAPIView.as_view()),
    path('post_detail/<int:pk>/',PostDetails.as_view()),
    path('comment_article/',CommentAPIView.as_view()),
    path('comment_detail/<int:pk>/',CommentAPIDetails.as_view())
]
