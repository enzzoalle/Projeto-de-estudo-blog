from django import forms

class ComentariosForm(forms.Form):
     titulo = forms.CharField(label='Título', max_length=55, widget=forms.TextInput(attrs={'id':'titulo-comentario', 'class': 'form-control', 'placeholder':'Título do comentário'}))
     comentario = forms.CharField(label='Comentar', max_length=1000, widget=forms.Textarea(attrs={'id':'conteudo-comentario', 'class': 'form-control', 'placeholder':'Conteúdo do comentário'}))