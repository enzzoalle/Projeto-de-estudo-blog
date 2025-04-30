from django.shortcuts import render
from .models import Post, Comentario
from .forms import ComentariosForm

def index(request):
     post = Post.objects.order_by('-data_post').first()
     comentarios = Comentario.objects.filter(post=post)

     form = ComentariosForm()
     context = {'form':form, 'post':post, 'comentarios':comentarios}
     return render(request, 'blogs/index.html', context)

def post_unique(request):
     return render(request, 'blogs/post_unique.html')

def posts(request):
     return render(request, 'blogs/posts.html')

def search(request):
     return render(request, 'blogs/search.html')