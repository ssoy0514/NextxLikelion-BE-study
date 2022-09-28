from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
#10
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
#5
# @csrf_exempt 10 이후로 불필요!


#11
from rest_framework.views import APIView

class ArticleAPIView(APIView):
    def get(self,request):
        articles = Article.objects,all()
        serializer = ArticleSerializer(articles, many=True) 
        return Response(serializer.data)
    
    def post(self, request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
    
    def get_object(self,id):
        try:
            return Article.object.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self,request,id ):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','PUT'])
def article_list(request):
    
    if request.method == 'GET':
        articles = Article.objects,all()
        serializer = ArticleSerializer(articles, many=True) #serializer는 한개의 객체만 이해할 수 있기 때문에 many=True
        # return JsonResponse(serializer.data, safe=False) api view 사용하면서 불필요
        return Response(serializer.data)
        #Response는 TemplateResponse 객체의 일종으로 렌더링되지 않은 컨텐츠를 가져오고 클라이언트에게 반환할 올바른 컨텐츠 유형을 결정
    
    elif request.method == "POST":
        # data = JSONParser().parse(request) api view 사용하면서 불필요
        # serializer = ArticleSerializer(data=data)
        serializer=ArticleSerializer(data=request.data)
        # request.data는 DRF 제공 -> 기능은 request.POST와 유사하지만 웹 API에 더 유용한 속성
        # 렌더링되지 않은 콘텐츠를 가져오고 클라이언트에게 반환할 올바른 컨텐츠 유형을 결정!
        # 즉 마구잡이로 보낸 serializer.data를 각 목적에 맞게 보여줄 수 있도록 함
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#8
# @csrf_exempt
@api_view(['GET','PUT','DELETE'])
def article_detail(request, pk):
    try:
        article = Article.object.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    # pk에 해당하는 post가 존재하는지/없으면 404
    if request.method =="GET":
        # articles = Article.objects.all() 하나만 봐도 ㄱㅊ many=True 불필요
        serializer = ArticleSerializer(article)
        # return JsonResponse(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=request.data)
        # request 요청이 들어온 그 post를 serializer틀에 담아 가져옴
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    