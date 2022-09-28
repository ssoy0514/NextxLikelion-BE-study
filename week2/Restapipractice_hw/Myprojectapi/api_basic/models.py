from django.db import models
#2
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.title