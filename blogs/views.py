from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Post, Comentario
from .forms import ComentariosForm
import os
from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Q

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

def posts(request):
     posts = Post.objects.order_by('-data_post')
     paginator = Paginator(posts, 5)
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)

     pages = []

     for page in range(int(page_number), int(page_number)+10):
          if page <= int(paginator.num_pages):
               pages.append(page)

     if int(page_number) > 1:
          anterior = int(page_number) - 1
     else:
          anterior = 1

     if int(page_number) < int(paginator.num_pages):
          proximo = int(page_number) + 1
     else:
          proximo = int(page_number)

     context = {'page_obj':page_obj, 'pages':pages, 'anterior':anterior, 'proximo':proximo}
     return render(request, 'blogs/posts.html', context)

def post_unique(request, id):
     post = get_object_or_404(Post, id=id)
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
                         return render(request, 'blogs/post_unique.html', context)
                    
                    if filtro_ofensas(conteudo):
                         form.add_error ('comentario', 'Seu comentário pode conter palavras ou expressões ofensivas!')
                         context = {'form':form, 'post':post, 'comentarios':comentarios}
                         return render(request, 'blogs/post_unique.html', context)
               
                    novo_comentario = Comentario(titulo=titulo, conteudo=conteudo, autor=autor, post=post)
                    novo_comentario.save()
                    return redirect(reverse('post_unique', kwargs={'id':id}))
               
               else:
                    context = {'form':form, 'post':post, 'comentarios':comentarios}
                    return render(request, 'blogs/post_unique.html', context)

     form = ComentariosForm()
     context = {'form':form, 'post':post, 'comentarios':comentarios}
     return render(request, 'blogs/post_unique.html', context)

def search(request):

     if request.method == 'POST':
          busca = request.POST.get('busca')
          posts = Post.objects.filter(Q(titulo__icontains=busca)| Q(conteudo__icontains=busca)).order_by('-data_post')
     else:
          posts = ''
          
     context = {'posts':posts}
     return render(request, 'blogs/search.html', context)