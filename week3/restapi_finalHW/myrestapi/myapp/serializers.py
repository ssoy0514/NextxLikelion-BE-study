from rest_framework import serializers
from .models import Major,User,Category,Post,Comment

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['name']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
        
class PostSerializer(serializers.ModelSerializer):
    #얘도...뭔지
    likes_count = serializers.SerializerMethodField(method_name='get_likes_count')
    is_liked = serializers.SerializerMethodField(method_name='get_is_liked')
    class Meta:
        model = Post
        fields = '__all__'
    #이건 뭘 위해???
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = CategorySerializer(instance.category).data
        response['author'] = UserSerializer(instance.author).data
        
        return response

    # serializerMethodField 반환값을 정의하는 함수
    def get_likes_count(self, obj):
        liked_users = obj.like_users.all()
        likes_count = liked_users.count()

        return likes_count

    # serializerMethodField 반환값을 정의하는 함수
    def get_is_liked(self, obj):
        user = self.context['request'].user

        if user and user in obj.like_users.all():
            return True
        else:
            return False