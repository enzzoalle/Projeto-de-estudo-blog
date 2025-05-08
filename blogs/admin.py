from django.contrib import admin
from .models import Post, Comentario
from .forms import PostForm

class PostAdmin(admin.ModelAdmin):
     form = PostForm

admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)