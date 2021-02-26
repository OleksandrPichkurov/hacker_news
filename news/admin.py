from django.contrib import admin
from .models import Vote, Comment, Post

# Register your models here.

admin.site.register(Vote)
admin.site.register(Comment)
admin.site.register(Post)
