from xml.etree.ElementTree import Comment
from django.db import models

# Create your models here.
class Major(models.Model):
    main = models.CharField(max_length=50)
    second = models.CharField(max_length=50)
    double = models.CharField(max_length=50)
    integrate = models.CharField(max_length=50)
    intensive = models.CharField(max_length=50)
    
class User(models.Model):
    ID = models.CharField(max_length=30)
    PW = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    major = models.ManyToManyField(Major)
    
class Comments(models.Model):
    comment = models.TextField()
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    comment = models.ForeignKey(Comments, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    
    
