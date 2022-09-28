#7
from django.urls import path
from .views import article_list,article_detail, ArticleAPIView,ArticleDetails

urlpatterns = [
    #12
    # path('article/',article_list),
    path('article/',ArticleAPIView.as_view()),
    #9
    # path('detail/<int:pk>/',article_detail) #함수형인 경우
    path('detail/<int:pk>/',ArticleDetails.as_view()) #클래스형이므로 view로 가져오기
    ]


