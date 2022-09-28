from django.db import models

# Create your models here.
class Major(models.Model):
    main = models.CharField(max_length=50) #본전공
    second = models.CharField(max_length=50) #이중
    double = models.CharField(max_length=50) #복수
    integrate = models.CharField(max_length=50) #융합
    intensive = models.CharField(max_length=50) #심화
    
class User(models.Model):
    user_ID = models.CharField(max_length=30)
    user_PW = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    major = models.ManyToManyField(Major)
    
class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    comment = models.ForeignKey(Comment, null=True, on_delete=models.SET_NULL)
    like_users = models.ManyToManyField(Like)
    user_name = models.ForeignKey(User,
                            on_delete=models.CASCADE)
    category = models.OneToOneField(Category, null=True, on_delete=models.SET_NULL)
    
    
# #치즈 도우 토마토소스 파슬리      
# class Basic(models.Model):
#     name = models.CharField(max_length=20)
#     def __str__(self):
#         return self.name
    
# #양파 버섯
# class Common(models.Model):
#     name = models.CharField(max_length=20)
#     def __str__(self):
#         return self.name
    
# #페페로니 스테이크 파인애플 감자
# class Special(models.Model):
#     name = models.CharField(max_length=20)
#     def __str__(self):
#         return self.name
# #음료
# class Drinks(models.Model):
#     name = models.CharField(max_length=20)
#     def __str__(self):
#         return self.name
    
# class Pizza(models.Model):
#     name = models.CharField(max_length=20)
#     basic_ingredients = models.ManyToManyField(Basic)
#     common_ingredients = models.ForeignKey(Common, on_delete=models.CASCADE)
#     special_ingredients = models.OneToOneField(Special,on_delete=models.CASCADE,primary_key=True)
#     drinks = models.ForeignKey(Drinks, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# #1대N 관계에선 foreignkey


























