from django.shortcuts import render

def login_view(request):
     return render(request, 'index')

def logout_view(request):
     return render(request, 'index')
