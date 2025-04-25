from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
     """Modelo de post"""
     titulo = models.CharField(max_length=55) # caixa de texto para o titulo com limite de 55 caracteres
     conteudo = models.TextField(max_length=200) # caixa de texto para o conteudo com limite de 200 caracteres
     data_post = models.DateTimeField(auto_now_add=True) # para que a data do post seja inserida automaticamente
     autor = models.ForeignKey(User, on_delete=models.CASCADE) # autor está vinculado ao User e quando o User é deletado, todos os posts tambem serão
     imagem_capa = models.ImageField(upload_to='images/', null=True)

     def __str__(self):
         return "Título: " + self.titulo + " | Autor: " + self.autor.first_name + " " + self.autor.last_name
     
class Comentario(models.Model):
     """Modelo de comentários"""
     titulo = models.CharField(max_length=55)
     conteudo = models.TextField(max_length=200)
     data_post = models.DateTimeField(auto_now_add=True)
     autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # para quando o autor for deletado, os comentarios permaneçam, mas com autor 'nulo'
     post = models.ForeignKey(Post, on_delete=models.CASCADE)

     def __str__(self):
         return "Título: " + self.titulo + " | Autor: " + self.autor.first_name + " " + self.autor.last_name + " | Post: " + self.post.titulo