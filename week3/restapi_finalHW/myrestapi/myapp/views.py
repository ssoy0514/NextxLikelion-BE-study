from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MajorSerializer,UserSerializer,CategorySerializer,PostSerializer,CommentSerializer
from .models import Major,User,Category,Post,Comment
# Create your views here.
class PostAPIView(APIView):
    def get(self,request):
        articles = Post.objects,all()
        serializer = PostSerializer(articles, many=True) 
        return Response(serializer.data)
    
    def post(self, request):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetails(APIView):
    
    def get_object(self,id):
        try:
            return Post.object.get(id=id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,requst,id):
        article = self.get_object(id)
        serializer = PostSerializer(article)
        return Response(serializer.data)
    
    def put(self,request,id ):
        article = self.get_object(id)
        serializer = PostSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CommentAPIView(APIView):
    def get(self,request):
        articles = Comment.objects,all()
        serializer = CommentSerializer(articles, many=True) 
        return Response(serializer.data)
    
    def post(self, request):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentAPIDetails(APIView):
    
    def get_object(self,id):
        try:
            return Comment.object.get(id=id)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,requst,id):
        article = self.get_object(id)
        serializer = CommentSerializer(article)
        return Response(serializer.data)
    
    def put(self,request,id ):
        article = self.get_object(id)
        serializer = CommentSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#게시판 글 작서하고 댓글 작성은 crud가 필요한데 나머지 major,user,category 정보는 어떻게..?
#댓글은 게시글 별로 다른거 아닌가...그럼 id값이 어떻게 되는건가..?
# +로그인 회원가입