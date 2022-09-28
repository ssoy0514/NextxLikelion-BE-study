from django.contrib import admin
from .models import Major,User,Category,Post,Comment
# Register your models here.
admin.site.register(Major)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)