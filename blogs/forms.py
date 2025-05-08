from django import forms
from .models import Post
from django.contrib.auth.models import User

class ComentariosForm(forms.Form):
     titulo = forms.CharField(label='Título', max_length=55, widget=forms.TextInput(attrs={'id':'titulo-comentario', 'class': 'form-control', 'placeholder':'Título do comentário'}))
     comentario = forms.CharField(label='Comentar', max_length=1000, widget=forms.Textarea(attrs={'id':'conteudo-comentario', 'class': 'form-control', 'placeholder':'Conteúdo do comentário'}))

class PostForm(forms.ModelForm):
     class Meta:
          model = Post
          fields = ['titulo', 'conteudo', 'autor', 'imagem_capa']

     def __init__(self, *args, **kwargs):
          super(PostForm, self).__init__(*args, **kwargs)
          self.fields['autor'].queryset = User.objects.filter(is_staff=True) # para mostrar apenas admins em autor lá no painel administrativo