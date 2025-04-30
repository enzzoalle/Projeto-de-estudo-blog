from django.shortcuts import render, redirect
from .models import Post, Comentario
from .forms import ComentariosForm
import os
from django.conf import settings

def filtro_ofensas(texto):
     texto = texto.lower()
     palavras_proibidas = os.path.join(settings.BASE_DIR, 'blogs', 'palavras_proibidas.txt')

     with open(palavras_proibidas, 'r', encoding='utf-8') as arquivo:
          for palavra in arquivo:
               palavra = palavra.strip()

               if palavra in texto:
                    return True
     return False

def index(request):
     post = Post.objects.order_by('-data_post').first()
     comentarios = Comentario.objects.filter(post=post)

     if request.user.is_authenticated:
          if request.method == 'POST':
               form = ComentariosForm(request.POST)

               if form.is_valid():
                    autor = request.user
                    titulo = form.cleaned_data['titulo']
                    conteudo = form.cleaned_data['comentario']

                    if filtro_ofensas(titulo):
                         form.add_error('titulo', 'Seu título pode conter palavras ou expressões ofensivas!')
                         context = {'form':form, 'post':post, 'comentarios':comentarios}
                         return render(request, 'blogs/index.html', context)
                    
                    if filtro_ofensas(conteudo):
                         form.add_error ('comentario', 'Seu comentário pode conter palavras ou expressões ofensivas!')
                         context = {'form':form, 'post':post, 'comentarios':comentarios}
                         return render(request, 'blogs/index.html', context)
               
                    novo_comentario = Comentario(titulo=titulo, conteudo=conteudo, autor=autor, post=post)
                    novo_comentario.save()
                    return redirect('index')
               
               else:
                    context = {'form':form, 'post':post, 'comentarios':comentarios}
                    return render(request, 'blogs/index.html', context)

     form = ComentariosForm()
     context = {'form':form, 'post':post, 'comentarios':comentarios}
     return render(request, 'blogs/index.html', context)

def post_unique(request):
     return render(request, 'blogs/post_unique.html')

def posts(request):
     return render(request, 'blogs/posts.html')

def search(request):
     return render(request, 'blogs/search.html')