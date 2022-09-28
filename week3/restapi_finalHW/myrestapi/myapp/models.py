from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class User(models.Model):
    user_ID = models.CharField(max_length=30,unique=True)
    user_PW = models.CharField(max_length=50)
    # name = models.CharField(max_length=20) 굳이 이름은 필요 없을 듯
    major = models.ManyToManyField(Major)
    def __str__(self):
        return self.user_ID

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    like_users = models.ManyToManyField(User,related_name="liked_posts", blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    category = models.OneToOneField(Category, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments") #1대다 관계는 foreignkey
    comment = models.TextField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 필요한가..? 보류
