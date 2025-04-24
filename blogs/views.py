from django.shortcuts import render

def index(request):

     context = {'teste': 'Esse é um teste para verificar se as variáveis de contexto funcionam.'}
     return render(request, 'blogs/index.html', context)

def post_unique(request):
     return render(request, 'blogs/post_unique.html')

def posts(request):
     return render(request, 'blogs/posts.html')

def search(request):
     return render(request, 'blogs/search.html')