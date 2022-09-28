#RESTful Framework 에서 JSON 으로 데이터를 전달하기 위한 serializer 
from rest_framework import serializers
from .models import Article

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length = 100)
#     author = serializers.CharField(max_length = 100)
    
#     def create(self,validated_data):
#         #유효성 검사를 통과한 데이터들을 바탕으로 
#         #새로운 DB 인스턴스를 생성하고 반환
#         return Article.objects.create(validated_data)
    
#     def update(self,instance, validated_data):
#         # 유효성 검사를 통과한 데이터들을 바탕으로 
#         #기존의 DB 인스턴스를 수정하고 반환
#         instance.title = validated_data.get('title',instance.title)
#         instance.author = validated_data.get('author',instance.author)
        
#         instance.save()
#         return instance

# modelserializer 사용하면 Serializer를 만들시, 모델에 기반하여 Seriliazer 필드를 자동으로 만들어줌, create/update 따로 정의할 필요 X
#4
class ArticleSerializer(serializers.ModelSerializer):
    class Meta :
        model = Article
        fields = ['id', 'title','author']